from src.workflow.units.execution import BaseExecutionUnit


class VaspExecutionUnit(BaseExecutionUnit):
    """
    Vasp execution unit parser class.
    """

    def __init__(self, config, work_dir):
        super(VaspExecutionUnit, self).__init__(config, work_dir)
