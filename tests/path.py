"""
A micro lib made for listing and 
returning element of a directory
as a list
"""

from os import walk

def elements(path: str) -> list:
    """_summary_

    Args:
        path (str): The path of the folder whose elements you want to know.

    Returns:
        list: The elements in the given path directory.
    """

    files = []

    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        files.extend(dirnames)
        break

    return files