from src.job.compute import BaseComputeParser


class SLURMComputeParser(BaseComputeParser):
    """
    Slurm compute parser class.
    """

    def __init__(self, work_dir):
        super(SLURMComputeParser, self).__init__(work_dir)
