import os

from src.utils import read_json

# JOB SETTINGS
OWNER = "demo"
CREATOR = "demo"
PROJECT = "demo-default"
JOB_NAME = "External Job"

# Type of Resource Management System (RMS), PBS or SLURM
RMS_TYPE = "PBS"

# List of data handlers, STDOUT, DISK and EXABYTE
DATA_HANDLERS = ["EXABYTE"]

# WORKFLOW SETTINGS
WORKFLOW_TEMPLATE_NAME = "shell.json"
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
WORKFLOW_TEMPLATE = read_json(os.path.join(TEMPLATES_DIR, WORKFLOW_TEMPLATE_NAME))

VASP_XML_FILE = "vasprun.xml"
ESPRESSO_XML_FILE = "data-file.xml"

DISK_DATA_HANDLER_DATA_DIR_NAME = ".exabyte"

# List of properties to extract
PROPERTIES = [
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
