from src.workflow.units.execution import BaseExecutionUnit


class EspressoExecutionUnit(BaseExecutionUnit):
    """
    Espresso execution unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(EspressoExecutionUnit, self).__init__(config, work_dir)
