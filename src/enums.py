ESPRESSO_EXECUTABLE_NAME_REGEX = r'\s+Program (.*) v.* starts on .*'
ESPRESSO_INPUT_FILE_REGEX = r'&CONTROL|&SYSTEM|&ELECTRONS|&IONS|&CELL|&BANDS|&INPUT|&PROJWFC|&DOS|'

ESPRESSO_EXECUTABLE_NAME_MAP = {
    "PWSCF": "pw.x",
    "BANDS": "bands.x",
    "MATDYN": "matdyn.x",
    "DYNMAT": "dynmat.x",
    "Q2R": "q2r.x",
    "PHONON": "ph.x",
    "PROJWFC": "projwfc.x",
    "DOS": "dos.x",
    "NEB": "neb.x",
}

ESPRESSO_DEFAULT_VERSION = "5.4.0"
ESPRESSO_SUPPORTED_VERSIONS = ["5.2.1", "5.4.0", "6.0.0", "6.3"]

VASP_DEFAULT_VERSION = "5.4.4"
VASP_SUPPORTED_VERSIONS = ["5.3.5", "5.4.4"]

SHELL_DEFAULT_VERSION = "4.2.46"
SHELL_SUPPORTED_VERSIONS = ["4.2.46"]

OUTPUT_CHUNK_SIZE = 1024 * 1024  # in bytes
