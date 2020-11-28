import os

import configparser

ExaParserConfig = configparser.ConfigParser(allow_no_value=True)
ExaParserConfig.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config"))
