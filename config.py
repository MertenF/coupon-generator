words_file = 'data/words.txt'
random_seed = 'Vlaamse 2023'


text = {
     'body': [
         '',
         '',
         '<font size=18><b>Werknemersbon VLMS KRMS</b></font>',
         '<font size=13>Code: <font face="Verdana"><b>{code}</b></font></font>'
         f'{"&nbsp; "*14}'
         '<font size=13>Waarde: <b>€{discount}</b></font>',
         '<i>Enkel te gebruiken in het <b>restaurant</b>!</i>',
         # '<font size=12>Enkel te gebruiken in het restaurant</font>',
         '<u>Bestellen via QR</u>: Bij de keuze van uw betaalmethode kan je de kortingscode toepassen.',
         '<u>Bestellen aan kassa</u>: Deze bon afgeven aan de kassa.',
         '',
         'Opgelet, kortingscode kan slechts <u>1 keer</u> gebruikt worden. ',
         'Zorg dat je een bestelling plaatst voor het gehele bedrag. '
         'Bij bestelling onder de € {discount} gaat het restbedrag verloren. ',
         '',
         'Ga naar de kassa indien je <u>meerdere kortingscodes</u> wil cumuleren in 1 bestelling. '
         'Je kan zelf geen meerdere kortingscodes in 1 bestelling verwerken.',
         '',
         '',
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
        'name': 'Restaurant',
        'prefix': '',
        'amount': 500,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto10.pdf',
        'discount_eur': 10,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
    {
        'name': 'Restaurant',
        'prefix': '',
        'amount': 24,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto20.pdf',
        'discount_eur': 20,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
    {
        'name': 'Restaurant',
        'prefix': '',
        'amount': 12,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto30.pdf',
        'discount_eur': 30,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
    {
        'name': 'Restaurant',
        'prefix': '',
        'amount': 12,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto40.pdf',
        'discount_eur': 40,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
    {
        'name': 'Restaurant',
        'prefix': '',
        'amount': 6,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto50.pdf',
        'discount_eur': 50,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
    {
        'name': 'Restaurant',
        'prefix': '',
        'amount': 6,
        'csv_file': 'output/vlaamse2023_korting_resto.csv',
        'pdf_file': 'output/vlaamse2023_resto60.pdf',
        'discount_eur': 60,
        'mode': 'Absolute',
        'use': 'SingleUse',
        'text': text,
    },
]





















