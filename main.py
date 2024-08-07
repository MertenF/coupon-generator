import os
import csv
from pprint import pprint

import config
import pdf_cards


def print_coupon_info(c_config, c_billy):
    print(f"Kortingcodes {c_config['name']}: Created={c_billy[0]['CREATED AT']} "
          f"Aantal={len(c_billy)} Korting=€{c_billy[0]['TOTAL AMOUNT']} "
          f"CSV={c_config['billy_codes']} PDF={c_config['pdf_file']}"
          )


def delete_files(key):
    files = {c[key] for c in config.coupons}
    for f in files:
        try:
            os.remove(f)
        except:
            pass


def read_codes(file: str):
    with open(file, newline='') as csvfile:
        return csv.DictReader(csvfile)


def main():
    delete_files('pdf_file')

    for coupon in config.coupons:
        with open(coupon['billy_codes'], newline='') as coupon_file:
            vouchers = list(csv.DictReader(coupon_file))
            pprint(vouchers)
        print_coupon_info(coupon, vouchers)

        coupon_codes = [row['CODE'] for row in vouchers]

        pdf_cards.create_pdf(
            filename=coupon['pdf_file'],
            codes=coupon_codes,
            discount=vouchers[0]['TOTAL AMOUNT'],
            text=coupon['text']
        )

    print('All codes, csv files, pdf file have been generated!')
    print('You can find them in the output folder')
    print('Exiting now...')


if __name__ == '__main__':
    main()
