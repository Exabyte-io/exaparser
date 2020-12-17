import click

from .config import ExaParserConfig
from .data.factory import get_data_handler
from .job import Job


@click.group()
@click.option('-c', '--config', help='full path to config file', type=click.Path(exists=True))
def main(config):
    if config:
        ExaParserConfig.read(config)


@main.command()
@click.argument('name')
@click.argument('work-dir', type=click.Path(exists=True, file_okay=False, resolve_path=True))
def job(name, work_dir):
    """Parse a job.

    Parses the output of job with NAME in directory WORK_DIR. For example:

        ./bin/exaparser job-123 /path/to/workdir/
    """
    job = Job(name, work_dir)
    for handler in ExaParserConfig.get("global", "data_handlers").replace(" ", "").split(","):
        get_data_handler(handler, job).handle()
