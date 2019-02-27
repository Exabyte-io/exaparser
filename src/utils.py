import json


def read(path):
    """
    Reads and returns the content of given file.

    Args:
        path (str): file path.

    Returns:
        str: file content.
    """
    with open(path) as f:
        return f.read()


def write_json(path, content):
    """
    Writes a given JSON content.

    Args:
        path (str): file path.
        content (dict): content.
    """
    with open(path, "w+") as f:
        f.write(json.dumps(content, indent=4))


def read_json(path):
    """
    Reads and returns the content of given file in JSON format.

    Args:
        path (str): file path.

    Returns:
        dict: file content.
    """
    return json.loads(read(path))
