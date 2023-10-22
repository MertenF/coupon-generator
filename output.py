import csv
from pathlib import Path

HEADER = ['code', 'mode', 'absolute', 'use']
# code = kortingscode
# mode = 'Absolute'
# absolute = discount in cents
# use: 'SingleUse' or 'MultiUse'
# from epoch time
# to epoch time


def write_csv(filename, *args, **kwargs):
    path = Path(filename)
    _write_csv(
        filename=filename,
        append=path.is_file(),
        *args, **kwargs
    )


def _write_csv(filename, append, codes, mode, discount, use):
    default_row = {
        'code': '',
        'mode': mode,
        'absolute': int(discount*100),
        'use': use,
    }
    if append:
        file_mode = 'a'
    else:
        file_mode = 'w'

    with open(filename, mode=file_mode, newline='') as f:
        writer = csv.DictWriter(f, HEADER)
        if not append:
            writer.writeheader()

        for code in codes:
            writer.writerow({**default_row, 'code': code})
