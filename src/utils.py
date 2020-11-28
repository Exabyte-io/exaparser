import json
import os
import re

import requests


def find_file(name, path):
    """
    Finds file with the specified name in the given path.

    Args:
        name (str): file name.
        path (str): starting path for search.

    Returns:
        str: absolute file path (if found)
    """
    for root, dirs, files in os.walk(path, followlinks=True):
        for file in files:
            if name in file:
                return os.path.join(root, file)


def find_file_with_pattern(pattern, path):
    """
    Finds a file inside a given directory that matches the pattern.

    Args:
        path (str): starting path for search.
        pattern (str): regex to apply on the file content.

    Returns:
        str: absolute file path
    """
    for root, dirs, files in os.walk(path, followlinks=True):
        for file_ in files:
            with open(os.path.join(root, file_)) as f:
                if re.match(pattern, f.read()):
                    return os.path.join(root, file_)


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


def upload_file_to_object_storage(file_):
    """
    Uploads a given file to object storage.

    Note: a new line is added to the file if it is empty.

    Args:
        file_ (dict): a dictionary with path and presignedURL keys.
    """
    path = file_["path"]
    session = requests.Session()
    if os.path.getsize(path) == 0:
        with open(path, 'w+') as f:
            f.write('\n')
    headers = {"Content-Length": str(os.path.getsize(path))}
    with open(path) as f:
        session.request("PUT", file_["URL"], data=f, headers=headers).raise_for_status()
