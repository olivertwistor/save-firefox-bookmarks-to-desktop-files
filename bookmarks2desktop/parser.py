"""
This script file deals with parsing a Firefox bookmark file.
"""
import json
from typing import Optional, Union

from bookmarks2desktop import bookmark, folder


def parse_json(bookmarks_file: str) -> dict:
    """
    Parses a JSON formatted Firefox bookmarks file into a dict.

    :param bookmarks_file: path to a JSON formatted Firefox bookmarks file

    :return: A dict that corresponds to the bookmarks file.

    :raises JSONDecodeError: if the supplied file isn't valid JSON.
    """
    with open(bookmarks_file, "r") as fp:
        return json.load(fp)


def create_directories_and_desktop_files(json_dict: dict,
                                         current_path: str = None) -> None:
    """
    Takes a parsed Firefox bookmark file and recursively creates directories
    and desktop files on the file system, as appropriate.

    :param json_dict: a Firefox bookmark file parsed into a JSON dict.
    :param current_path: current file system path where directories and desktop
    files are to be added; defaults to None, which means current working
    directory
    """
    raw_type_code = json_dict.get("typeCode")
    if raw_type_code is None:
        return

    type_code = int(raw_type_code)
    if bookmark.is_bookmark(type_code):
        pass
    elif folder.is_folder(type_code):
        pass
