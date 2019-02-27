from src.workflow.units.execution import BaseExecutionUnit


class EspressoExecutionUnit(BaseExecutionUnit):
    """
    Espresso execution unit parser class.
    """

    def __init__(self, config, work_dir):
        super(EspressoExecutionUnit, self).__init__(config, work_dir)
