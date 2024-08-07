

text = {
     'body': [
         '',
         '',
         '<font size=24><b>Medewerkersbon</b></font>',
         '<font size=14>VLMS KRMS 2024 - Scouts WVB</font>',
         '',
         '<font size=14>Code: <font face="Verdana"><b>{code}</b></font></font>'
         f'{"&nbsp; "*10}'
         '<font size=14>Waarde: <b>€{discount}</b></font>',
         '<u>Bestellen aan kassa</u>: Deze bon afgeven aan de kassa.',

         '<u>Bestellen via QR</u>:',
         '1) Scan de QR op tafel of de QR onderaan deze bon',
         '2) Plaats je bestelling',
         '3) Voer je code in bij "<i>Kortingscode Medewerker</i>"',
         '4) Betaal het resterende bedrag of klik op bevestigen als<br/>'
         '&nbsp;&nbsp;&nbsp; je bon de hele bestelling kan vergoeden',
         '',
         'Je kortingscode kan meerdere keren toegepast worden,<br/> tot de volledige waarde opgebruikt is.',
         '',
         '',
     ],
}
# coupons = [
#     {
#          'name': 'Mosselfeest',
#          'prefix': '',
#          'amount': 220,
#          'csv_file': 'output/mosselfeest_korting.csv',
#          'pdf_file': 'output/mosselfeest_korting10.pdf',
#          'discount_eur': 10,
#          'mode': 'Absolute',
#          'use': 'SingleUse',
#          'text': text
#     },
#     {
#         'name': 'Mosselfeest',
#         'prefix': '',
#         'amount': 50,
#         'csv_file': 'output/mosselfeest_korting.csv',
#         'pdf_file': 'output/mosselfeest_korting20.pdf',
#         'discount_eur': 20,
#         'mode': 'Absolute',
#         'use': 'SingleUse',
#         'text': text
#     },
# ]


coupons = [
    {
        'name': 'test',
        'billy_codes': 'data/test.csv',
        'pdf_file': 'output/test.pdf',
        'text': text,
    },
]





















