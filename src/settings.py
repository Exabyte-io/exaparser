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

# Workflow template settings
WORKFLOW_TEMPLATE_NAME = "shell.json"
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
WORKFLOW_TEMPLATE = read_json(os.path.join(TEMPLATES_DIR, WORKFLOW_TEMPLATE_NAME))

# Name of VASP XML file used to identify the job type
VASP_XML_FILE = "vasprun.xml"

# Name of Espresso XML file used to identify the job type
ESPRESSO_XML_FILE = "data-file.xml"

# Name of the directory to store the job if DISK data handler is enabled
DISK_DATA_HANDLER_DATA_DIR_NAME = ".exabyte"

# Exabyte RESTful API Data Handler Settings
# See https://docs.exabyte.io/rest-api/overview for more information.
API_HOSTNAME = "platform.exabyte.io"
API_PORT = 443
API_ACCOUNT_ID = "zX6Wf8QdQkgEpP26u"
API_AUTH_TOKEN = "8YpFg97E-zN17xP9bqngoGFJV8mBXT553zh8iE9a0nP"
API_SECURE = True
API_VERSION = "2018-10-01"

# Number of workers used for uploading files in parallel
NUM_WORKERS = 25

# Whether to upload files to object storage
UPLOAD_FILES = True

# Pattern to exclude files from being upload to object storage
EXCLUDED_FILES_REGEX = ""

# List of properties to extract. Parser tries to extract all properties by default.
# Comment out the ones that should not be extracted for particular job, e.g. band_structure in toal ennergy calculation.
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
