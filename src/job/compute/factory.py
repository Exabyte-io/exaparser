from .managers.pbs import PBSComputeParser
from .managers.slurm import SLURMComputeParser


def get_compute_parser(name, work_dir):
    """
    Returns an instance of compute parser class

    Args:
        name (str): parser name, PBS or SLURM.
        work_dir (str): full path to job working directory.
    """
    parsers = dict(PBS=PBSComputeParser, SLURM=SLURMComputeParser)
    return parsers[name](work_dir)
