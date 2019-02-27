from src.workflow.units.execution import BaseExecutionUnit


class VaspExecutionUnit(BaseExecutionUnit):
    """
    Vasp execution unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(VaspExecutionUnit, self).__init__(config, work_dir)
