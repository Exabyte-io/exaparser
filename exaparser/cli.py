import click

from .config import ExaParserConfig
from .data.factory import get_data_handler
from .job import Job


@click.group()
def main():
    pass


@main.command()
@click.option('-n', '--name', required=True, help='job name')
@click.option('-c', '--config', help='full path to config file')
@click.option('-w', '--work-dir', required=True, help='full path to working directory')
def job(name, config, work_dir):
    if config: ExaParserConfig.read(config)
    job = Job(name, work_dir)
    for handler in ExaParserConfig.get("global", "data_handlers").replace(" ", "").split(","):
        get_data_handler(handler, job).handle()
