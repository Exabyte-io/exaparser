import configparser
import os
from pathlib import Path


def find_config_file() -> Path:
    """
    Look in an ordered list of standard locations for the exaparser config file, and return the first one we find.
    If no config file is found, throw an Exception()
    """
    possible_filepaths = [
        Path(__file__) / '../../config',
        Path(os.path.expanduser('~')) / '.exabyte/exaparser/config',
        Path('/etc/exabyte/exaparser/config'),
    ]
    for path in possible_filepaths:
        path = path.resolve()
        if path.is_file():
            return path
    raise Exception('Could not find exaparser config file in any of the known locations.')


ExaParserConfig = configparser.ConfigParser(allow_no_value=True)
ExaParserConfig.read(find_config_file())
