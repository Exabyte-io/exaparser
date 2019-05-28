from src.workflow.units.execution import BaseExecutionUnit


class ShellExecutionUnit(BaseExecutionUnit):
    """
    Shell unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(ShellExecutionUnit, self).__init__(config, work_dir)

    @property
    def application(self):
        """
        Returns the application used in the unit.

        Returns:
             dict
        """
        return {
            "name": "shell",
            "summary": "Shell Script",
            "version": "4.2.46"
        }

    @property
    def executable(self):
        """
        Returns the executable used in the unit.

        Returns:
             dict
        """
        return {
            "name": "sh"
        }
