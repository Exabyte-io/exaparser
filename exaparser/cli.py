import argparse

from .config import ExaParserConfig
from .data.factory import get_data_handler
from .job import Job


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True, help='job name')
    parser.add_argument('-c', '--config', help='full path to config file')
    parser.add_argument('-w', '--work-dir', dest="work_dir", required=True, help='full path to working directory')
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.config:
        ExaParserConfig.read(args.config)
    job = Job(args.name, args.work_dir)
    for handler in ExaParserConfig.get("global", "data_handlers").replace(" ", "").split(","):
        get_data_handler(handler, job).handle()
