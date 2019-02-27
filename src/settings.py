import os

from src.utils import read_json

# JOB SETTINGS

OWNER = "demo"
CREATOR = "demo"
PROJECT = "demo-default"

RMS_TYPE = "PBS"

DATA_HANDLERS = ["stdout"]

JOB_PREFIX = ""

# WORKFLOW SETTINGS
WORKFLOW_TEMPLATE_NAME = "shell.json"
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
WORKFLOW_TEMPLATE = read_json(os.path.join(TEMPLATES_DIR, WORKFLOW_TEMPLATE_NAME))

VASP_XML_FILE = "vasprun.xml"
ESPRESSO_XML_FILE = "data-file.xml"

PROPERTIES = [
    "phonon_dos",
    "convergence_ionic",
    "pressure",
    "atomic_forces",
    "stress_tensor",
    "phonon_dispersions",
    "fermi_energy",
    "convergence_electronic",
    "density_of_states",
    "zero_point_energy",
    "total_energy_contributions",
    "total_force",
    "band_structure",
    "band_gaps",
    "total_energy"
]
