"""
This file deals with parsing bookmarks and saving them to the file system.
"""
import dataclasses
import os


@dataclasses.dataclass
class Bookmark:
    """
    Bookmark is the leaf nodes in the Firefox bookmark file. Among other
    things, it has a name and a URI.
    """
    title: str
    uri: str


def create_desktop_file(bookmark: Bookmark,
                        directory: str,
                        overwrite: bool = True) -> None:
    """
    Creates a desktop file on the file system, based on the provided Bookmark.

    :param bookmark: the Bookmark object to save to the file system
    :param directory: path to the directory in which to write the desktop file
    :param overwrite: whether to overwrite any file with the same path present
    on the file system
    """
    file_name = f"{os.path.join(directory, bookmark.title)}.desktop"
    if os.path.exists(file_name) and not overwrite:
        return

    with open(file_name, "w", encoding="utf-8") as fp:
        fp.writelines([
            "[Desktop Entry]",
            "Version=1.0",
            "Type=Link",
            f"Name={bookmark.title}",
            f"URL={bookmark.uri}"
        ])


def is_bookmark(type_code: int) -> bool:
    """
    Determines whether the provided type code signifies a bookmark.

    :param type_code: type code from a Firefox bookmarks file

    :return: True if it is a bookmark; False otherwise.
    """
    return type_code == 1
