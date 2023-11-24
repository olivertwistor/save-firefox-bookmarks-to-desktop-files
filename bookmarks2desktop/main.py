"""
This is the main script of this app. It contains the main program flow.
"""
from bookmarks2desktop import parser


def main() -> None:
    """
    Reads a JSON formatted Firefox bookmarks file into a dict. For each
    bookmark folder found, this app creates a directory on the file system.
    For each bookmark link, this app creates a .desktop file on the file
    system, in the respective directory. In essence, it recreates the entire
    bookmark file on the file system with the same hierarchy. After each
    successful write operation to the file system, the bookmark is deleted from
    the bookmark file.
    """
    json = parser.parse_json("tests/bookmarks.json")


if __name__ == "__main__":
    main()
