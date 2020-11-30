from express.parsers.apps.espresso.settings import XML_DATA_FILE as ESPRESSO_XML_FILE
from express.parsers.apps.vasp.settings import XML_DATA_FILE as VASP_XML_FILE

from exaparser.utils import find_file, find_file_with_pattern
from .shell import ShellExecutionUnit, ESPRESSO_INPUT_FILE_REGEX
from ..modeling import ModelingExecutionUnit


class ShellWithResultsExecutionUnit(ShellExecutionUnit, ModelingExecutionUnit):
    """
    Shell unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(ShellWithResultsExecutionUnit, self).__init__(config, work_dir)

    def _is_vasp_calculation(self):
        if find_file("INCAR", self.work_dir):
            return True
        if find_file("POSCAR", self.work_dir):
            return True
        if find_file(VASP_XML_FILE, self.work_dir):
            return True

    def _is_espresso_calculation(self):
        if find_file(ESPRESSO_XML_FILE, self.work_dir):
            return True
        if find_file_with_pattern(ESPRESSO_INPUT_FILE_REGEX, self.work_dir):
            return True

    @property
    def parser_name(self):
        """
        Returns the name of the parser to pass to ExPrESS.

        Returns:
             str: espresso or vasp
        """
        if self._is_vasp_calculation():
            return "vasp"
        if self._is_espresso_calculation():
            return "espresso"
