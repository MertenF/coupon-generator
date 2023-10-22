import os

import config
from coupon import CouponGenerator
import output
import pdf_cards


def print_coupon_info(c_info):
    print(f"Kortingcodes {c_info['name']}: Prefix={c_info['prefix']} "
          f"Aantal={c_info['amount']} Korting=€{c_info['discount_eur']} "
          f"CSV={c_info['csv_file']} "
          )


def delete_files(key):
    files = {c[key] for c in config.coupons}
    for f in files:
        try:
            os.remove(f)
        except:
            pass


def main():
    delete_files('csv_file')
    delete_files('pdf_file')

    generator = CouponGenerator()
    generator.random_seed(config.random_seed)

    for coupon in config.coupons:
        print_coupon_info(coupon)
        generator.set_prefix(coupon['prefix'])

        coupon_codes = [generator.generate_coupon() for _ in range(coupon['amount'])]

        output.write_csv(
            filename=coupon['csv_file'],
            codes=coupon_codes,
            mode=coupon['mode'],
            discount=coupon['discount_eur'],
            use=coupon['use'],
        )

        pdf_cards.create_pdf(
            filename=coupon['pdf_file'],
            codes=coupon_codes,
            discount=coupon['discount_eur'],
            text=coupon['text']
        )

    print('All codes, csv files, pdf file have been generated!')
    print('You can find them in the output folder')
    print('Exiting now...')


if __name__ == '__main__':
    main()