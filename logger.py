import logging

INFO = logging.INFO
WARN = logging.WARN
DEBUG = logging.DEBUG
ERROR = logging.ERROR
FATAL = logging.FATAL
CRITICAL = logging.CRITICAL

DEBUG_FORMAT = " - ".join(["%(asctime)s", "%(levelname)s", "%(filename)s", "%(message)s"])


def get_logger():
    """
    Returns a logger.

    Returns:
        logger
    """
    logger = logging.getLogger('dft-parser')
    logger.addHandler(logging.NullHandler())
    logger.setLevel(DEBUG)
    return logger


def configure_logger(console_debug=False):
    """
    Configures logger.

    Args:
        console_debug(bool): console logger in debug mode
    """
    formatter = logging.Formatter(DEBUG_FORMAT)

    console = logging.StreamHandler()
    console.setLevel(DEBUG) if console_debug else console.setLevel(INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)


logger = get_logger()
