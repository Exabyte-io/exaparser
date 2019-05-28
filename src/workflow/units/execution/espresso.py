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

    @property
    def application(self):
        """
        Returns the application used in the unit.

        Returns:
             dict
        """
        return {
            "name": "espresso",
            "version": "5.4.0",
            "summary": "Quantum Espresso"
        }

    @property
    def executable(self):
        """
        Returns the executable used in the unit.

        Returns:
             dict
        """
        return {
            "name": "pw.x"
        }
