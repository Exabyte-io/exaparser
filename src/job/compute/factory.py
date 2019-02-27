from src.job.compute.pbs import PBSComputeParser
from src.job.compute.slurm import SLURMComputeParser


def get_compute_parser(RMS="PBS/Torque", *args, **kwargs):
    parsers = dict(PBS=PBSComputeParser, SLURM=SLURMComputeParser)
    return parsers[RMS](*args, **kwargs)
