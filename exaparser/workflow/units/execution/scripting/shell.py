from exaparser.enums import *
from . import ScriptingExecutionUnit


class ShellExecutionUnit(ScriptingExecutionUnit):
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
            "version": self.version
        }

    @property
    def version(self):
        """
        Returns the application version used in the unit.

        Returns:
             str
        """
        return SHELL_DEFAULT_VERSION

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
