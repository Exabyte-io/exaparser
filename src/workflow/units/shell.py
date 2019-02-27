import os

from src.utils import read
from src.workflow.units.execution import BaseExecutionUnit


class ShellExecutionUnit(BaseExecutionUnit):
    """
    Shell unit parser class.
    """

    def __init__(self, config, work_dir):
        super(ShellExecutionUnit, self).__init__(config, work_dir)

    @property
    def application(self):
        return {
            "name": "shell",
            "summary": "Shell Script",
            "version": "4.2.46"
        }

    @property
    def executable(self):
        return {
            "name": "sh"
        }

    @property
    def inputs(self):
        return [
            {
                "isManuallyChanged": True,
                "name": self.config["name"],
                "rendered": read(os.path.join(self.work_dir, self.config["name"]))
            }
        ]
