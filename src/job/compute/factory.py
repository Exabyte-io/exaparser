from src.job.compute.managers.pbs import PBSComputeParser
from src.job.compute.managers.slurm import SLURMComputeParser


def get_compute_parser(name, work_dir):
    parsers = dict(PBS=PBSComputeParser, SLURM=SLURMComputeParser)
    return parsers[name](work_dir)
