from .. import BaseComputeParser


class PBSComputeParser(BaseComputeParser):
    """
    PBS/Torque compute parser class.

    Args:
        work_dir (str): full path to working directory.
    """

    def __init__(self, work_dir):
        super(PBSComputeParser, self).__init__(work_dir)
