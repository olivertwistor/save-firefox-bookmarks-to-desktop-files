"""
This file deals with parsing bookmark folders and saving them to the file
system as directories.
"""


def is_folder(type_code: int) -> bool:
    """
    Determines whether the provided type code signifies a bookmark folder.

    :param type_code: type code from a Firefox bookmarks file

    :return: True if it is a bookmark folder; False otherwise.
    """
    return type_code == 2
