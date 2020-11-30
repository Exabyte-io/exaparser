import re
import xml.etree.ElementTree as ET

from express.parsers.apps.espresso.settings import XML_DATA_FILE as ESPRESSO_XML_FILE

from exaparser.enums import *
from exaparser.utils import find_file
from . import ModelingExecutionUnit


class EspressoExecutionUnit(ModelingExecutionUnit):
    """
    Espresso execution unit parser class.

    Args:
        config (dict): unit config.
        work_dir (str): full path to working directory.
    """

    def __init__(self, config, work_dir):
        super(EspressoExecutionUnit, self).__init__(config, work_dir)
        self.xml_path = find_file(ESPRESSO_XML_FILE, self.work_dir)

    @property
    def parser_name(self):
        """
        Returns the name of the parser to pass to ExPrESS.

        Returns:
             str
        """
        return "espresso"

    @property
    def version(self):
        """
        Returns the application version used in the unit.

        Returns:
             str
        """
        root = ET.parse(self.xml_path).getroot()
        version = root.find('HEADER').find("CREATOR").attrib.get("VERSION").strip()
        return version if version in ESPRESSO_SUPPORTED_VERSIONS else ESPRESSO_DEFAULT_VERSION

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
