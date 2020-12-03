from .. import BaseComputeParser


class SLURMComputeParser(BaseComputeParser):
    """
    Slurm compute parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, work_dir):
        super(SLURMComputeParser, self).__init__(work_dir)
