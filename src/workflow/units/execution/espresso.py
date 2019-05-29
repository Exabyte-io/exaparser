import os
import re

from src.utils import find_file_with_pattern, read
from src.workflow.units.execution import BaseExecutionUnit
from src.enums import ESPRESSO_EXECUTABLE_NAME_REGEX, ESPRESSO_EXECUTABLE_NAME_MAP, ESPRESSO_INPUT_FILE_REGEX


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
    def stdout_file(self):
        stdout_file = super(EspressoExecutionUnit, self).stdout_file
        if os.path.exists(stdout_file): return stdout_file
        return find_file_with_pattern(self.work_dir, ESPRESSO_EXECUTABLE_NAME_REGEX)

    @property
    def version(self):
        """
        Returns the application version used in the unit.

        Returns:
             str
        """
        return "5.4.0"

    @property
    def application(self):
        """
        Returns the application used in the unit.

        Returns:
             dict
        """
        return {
            "name": "espresso",
            "version": self.version,
            "summary": "Quantum Espresso"
        }

    @property
    def executable(self):
        """
        Returns the executable used in the unit.

        Returns:
             dict
        """
        with open(self.stdout_file) as f:
            executable = ESPRESSO_EXECUTABLE_NAME_MAP[re.findall(ESPRESSO_EXECUTABLE_NAME_REGEX, f.read())[0]]
            return {
                "name": executable
            }

    @property
    def input(self):
        """
        Returns a list of input files used in the unit.

        Note: Make sure to set "isManuallyChanged" to True.

        Returns:
             list[dict]
        """
        input_ = os.path.join(self.work_dir, self.config.get("input", [])[0]["name"])
        if not os.path.exists(input_): input_ = find_file_with_pattern(self.work_dir, ESPRESSO_INPUT_FILE_REGEX)
        return [{
            "name": os.path.basename(input_),
            "isManuallyChanged": True,
            "rendered": read(input_)
        }]

    @property
    def input_file_names(self):
        name = self.config.get("input", [])[0]
        if os.path.join(self.work_dir, name): return [name]
        return [find_file_with_pattern(self.work_dir, ESPRESSO_INPUT_FILE_REGEX)]
