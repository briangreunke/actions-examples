from argparse import ArgumentParser
from datetime import datetime


parser = ArgumentParser()
parser.add_argument("-f", "--file", help="Name of output file", required=True)
args = parser.parse_args()


with open(args.file, "w") as f:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f'File updated at {now}')
