import os

from src.utils import read_json

# Job owner slug
OWNER_SLUG = "demo"

# Job project slug
PROJECT_SLUG = "demo-default"

# Job name
JOB_NAME = "External Job"

# Type of Resource Management System (RMS), PBS or SLURM
RMS_TYPE = "PBS"

# List of data handlers, STDOUT, DISK and ExabyteRESTFulAPI
DATA_HANDLERS = ["ExabyteRESTFulAPI"]

# WORKFLOW SETTINGS
WORKFLOW_TEMPLATE_NAME = "shell.json"
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
WORKFLOW_TEMPLATE = read_json(os.path.join(TEMPLATES_DIR, WORKFLOW_TEMPLATE_NAME))

VASP_XML_FILE = "vasprun.xml"
ESPRESSO_XML_FILE = "data-file.xml"

DISK_DATA_HANDLER_DATA_DIR_NAME = ".exabyte"

# Exabyte Data Handler Settings
API_HOSTNAME = "platform.exabyte.io"
API_PORT = 443
API_ACCOUNT_ID = "zX6Wf8QdQkgEpP26u"
API_AUTH_TOKEN = "8YpFg97E-zN17xP9bqngoGFJV8mBXT553zh8iE9a0nP"
API_SECURE = True
API_VERSION = "2018-10-01"

NUM_WORKERS = 25
UPLOAD_FILES = True
EXCLUDED_FILES_REGEX = ""
S3_REGION = "us-west-2"
S3_BUCKET = "exabyte-external"

# List of properties to extract
PROPERTIES = [
    "final_structure",
    "phonon_dos",
    "pressure",
    "atomic_forces",
    "stress_tensor",
    "phonon_dispersions",
    "fermi_energy",
    "density_of_states",
    "zero_point_energy",
    "total_energy_contributions",
    "total_force",
    "band_structure",
    "band_gaps",
    "total_energy"
]
