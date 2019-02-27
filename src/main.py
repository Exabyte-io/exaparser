import argparse

from src.job import Job


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--work-dir', dest="work_dir", required=True, help='full path to working directory')
    return parser.parse_args()


def main():
    args = parse_arguments()
    Job(args.work_dir).parse()
