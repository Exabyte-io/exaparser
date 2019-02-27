from src.job.compute.managers.pbs import PBSComputeParser
from src.job.compute.managers.slurm import SLURMComputeParser


def get_compute_parser(RMS="PBS/Torque", *args, **kwargs):
    parsers = dict(PBS=PBSComputeParser, SLURM=SLURMComputeParser)
    return parsers[RMS](*args, **kwargs)
