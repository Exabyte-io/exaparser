import os

from src.utils import read
from src.workflow.units import BaseUnit


class ShellUnit(BaseUnit):
    """
    Shell unit parser class.
    """

    def __init__(self, config, *args, **kwargs):
        super(ShellUnit, self).__init__(config, *args, **kwargs)

    @property
    def inputs(self):
        return [
            {
                "isManuallyChanged": True,
                "name": self.config["name"],
                "rendered": read(os.path.join(self.work_dir, self.config["name"]))
            }
        ]
