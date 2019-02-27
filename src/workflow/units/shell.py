import os

from src import settings
from src.utils import read, find_file
from src.workflow.units.execution import BaseExecutionUnit


class ShellExecutionUnit(BaseExecutionUnit):
    """
    Shell unit parser class.
    """

    def __init__(self, config, work_dir):
        super(ShellExecutionUnit, self).__init__(config, work_dir)

    @property
    def express_parser_name(self):
        if find_file(settings.VASP_XML_FILE, self.work_dir): return "vasp"
        if find_file(settings.ESPRESSO_XML_FILE, self.work_dir): return "espresso"

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
    def input(self):
        return [
            {
                "isManuallyChanged": True,
                "name": self.config["input"][0]["name"],
                "rendered": read(os.path.join(self.work_dir, self.config["input"][0]["name"]))
            }
        ]
