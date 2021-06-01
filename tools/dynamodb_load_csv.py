import asyncio
import argparse
import pathlib
import sys
import csv
import re
from io import StringIO
from typing import List

import aioboto3


parser = argparse.ArgumentParser(
    usage="%(prog)s [FILE]...",
    description="CSV files to load into DynamoDB."
)
parser.add_argument("-t", "--table", required=True)
parser.add_argument('files', nargs='*')


def process_file(filename: str) -> str:
    return pathlib.Path(filename).read_text()


async def load_csv(table_name: str, csv_data: str):
    csv_io = StringIO(csv_data)
    reader = csv.reader(csv_io, delimiter=',', quotechar='"')
    header_row = next(reader)
    keys = [re.sub(r'\s+\([A-Z]+\)$', '', k) for k in header_row]

    async with aioboto3.resource('dynamodb') as dynamodb:
        table = await dynamodb.Table(table_name)
        async with table.batch_writer() as batch:
            for row in reader:
                await batch.put_item(
                    Item=dict(zip(keys, row))
                )


async def main():
    args = parser.parse_args()
    for file in args.files:
        try:
            await load_csv(args.table, process_file(file))
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
