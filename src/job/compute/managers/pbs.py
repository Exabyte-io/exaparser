from src.job.compute import BaseComputeParser


class PBSComputeParser(BaseComputeParser):
    """
    PBS/Torque compute parser class.
    """

    def __init__(self, work_dir):
        super(PBSComputeParser, self).__init__(work_dir)
