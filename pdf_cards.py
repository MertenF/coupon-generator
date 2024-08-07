from barcode import Code128
from barcode.writer import SVGWriter, ImageWriter

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Image, Table, \
    TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


PAGE_HEIGHT = A4[1]
PAGE_WIDTH = A4[0]
MARGIN = 0.5*cm

BARCODE_WIDTH = 400
BARCODE_HEIGHT = 150
SCALE = 0.3

QR_SIZE = 70

styles = getSampleStyleSheet()

pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
pdfmetrics.registerFont(TTFont('VerdanaBold', 'Verdanab.ttf'))
pdfmetrics.registerFont(TTFont('VerdanaItalic', 'Verdanai.ttf'))
pdfmetrics.registerFont(TTFont('VerdanaBoldItalic', 'Verdanaz.ttf'))
pdfmetrics.registerFontFamily(
    'Verdana',
    normal='Verdana',
    bold='VerdanaBold',
    italic='VerdanaItalic',
    boldItalic='VerdanaBoldItalic',
)


def frame_list(rows, cols):
    usable_height = PAGE_HEIGHT-2*MARGIN
    usable_width = PAGE_WIDTH-2*MARGIN

    frame_height = usable_height/rows
    frame_width = usable_width/cols

    frames = []
    for col in range(cols):
        for row in range(rows-1, -1, -1):
            f = Frame(
                x1=frame_width*col + MARGIN,
                y1=frame_height*row + MARGIN,
                height=frame_height,
                width=frame_width,
                showBoundary=0,
            )
            frames.append(f)
    return frames


def generate_barcode(code: str) -> None:

    with open(f'img/{code}.png', 'wb') as barcode_image:
        barcode = Code128(code, writer=ImageWriter())
        options = {'write_text': False}
        barcode.write(barcode_image, options)


def create_pdf(filename, *args, **kwargs):
    doc = BaseDocTemplate(filename, showBoundary=0)
    page_template = PageTemplate(frames=frame_list(3, 2))
    doc.addPageTemplates(page_template)

    story = cards(*args, **kwargs)

    doc.build(story)
    print(f'PDF file {filename} has been generated!')


def cards(codes: list[str], discount: int, text: dict):
    story = []
    style = styles["Normal"]
    #style.fontName = 'Verdana'

    for code in codes:
        generate_barcode(code)

        variables = {
            'code': code,
            'discount': discount,
        }

        infolist = [line.format(**variables) for line in text['body']]
        info = '<br/>'.join(infolist)

        infopara = Paragraph(info, style)
        story.append(infopara)

        order_qr = Image('data/order-qr.png',
                          width=QR_SIZE,
                          height=QR_SIZE,
                          )

        barcode = Image(
            f'img/{code}.png',
            width=BARCODE_WIDTH*SCALE,
            height=BARCODE_HEIGHT*SCALE,
        )

        spacing = 50
        tstyle = TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
        ])
        table = Table(
            data=[
                [barcode, order_qr],
            ],
            colWidths=[BARCODE_WIDTH*SCALE+spacing, QR_SIZE],
            rowHeights=[40],
            hAlign='LEFT',
            vAlign='CENTER',
            style=tstyle,
        )
        story.append(table)


        #story.append(Spacer(1, 0*mm))

    return story
