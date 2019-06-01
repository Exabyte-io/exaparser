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

OUTPUT_CHUNK_SIZE = 1024 * 1024  # in bytes
