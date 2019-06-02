import os
import xml.etree.ElementTree as ET

from src.enums import *
from src.utils import find_file
from src.config import ExaParserConfig
from src.workflow.units.execution import BaseExecutionUnit


class VaspExecutionUnit(BaseExecutionUnit):
    """
    Vasp execution unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(VaspExecutionUnit, self).__init__(config, work_dir)
        self.xml_path = find_file(ExaParserConfig["global"]["vasp_xml_file"], self.work_dir)

    @property
    def stdout_file(self):
        stdout_file = super(VaspExecutionUnit, self).stdout_file
        return stdout_file if os.path.exists(stdout_file) else os.path.join(self.work_dir, "OUTCAR")

    @property
    def application(self):
        """
        Returns the application used in the unit.

        Returns:
             dict
        """
        return {
            "name": "vasp",
            "version": self.version,
            "summary": "Vienna Ab-initio Simulation Package"
        }

    @property
    def version(self):
        """
        Returns the application version used in the unit.

        Returns:
             str
        """
        root = ET.parse(self.xml_path).getroot()
        version = root.find('generator').find('.//i[@name="version"]').text.strip()
        return version if version in VASP_SUPPORTED_VERSIONS else VASP_DEFAULT_VERSION

    @property
    def executable(self):
        """
        Returns the executable used in the unit.

        Returns:
             dict
        """
        return {
            "name": "vasp"
        }
