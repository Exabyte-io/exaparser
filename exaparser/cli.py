import click

from .config import ExaParserConfig
from .data.factory import get_data_handler
from .job import Job


@click.group()
@click.pass_context
@click.option('-c', '--config', help='full path to config file', type=click.Path(exists=True))
def main(ctx, config):
    if config:
        ExaParserConfig.read(config)
    ctx.ensure_object(dict)
    ctx.obj['handlers'] = ExaParserConfig.get("global", "data_handlers").replace(" ", "").split(",")


@main.command()
@click.pass_context
@click.argument('name')
@click.argument('work-dir', type=click.Path(exists=True, file_okay=False, resolve_path=True))
def job(ctx, name, work_dir):
    """Parse a job.

    Parses the output of job with NAME in directory WORK_DIR. For example:

        ./bin/exaparser job-123 /path/to/workdir/
    """
    job = Job(name, work_dir)
    for handler in ctx.obj['handlers']:
        get_data_handler(handler, job).handle()


@main.command()
@click.pass_context
@click.argument('work-dir', type=click.Path(exists=True, file_okay=False, resolve_path=True))
def structures(ctx, work_dir):
    """Parse a working directory for structure(s) data.

    Example:

        ./bin/exaparser /path/to/workdir/with/structure/data
    """
    ctx.forward(job, name='structures')
