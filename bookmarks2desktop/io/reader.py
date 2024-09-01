import json

from bookmarks2desktop.exceptions import InvalidBookmarksDictError
from bookmarks2desktop.tree.node import Node


class Reader:
    """
    This class is responsible for reading Firefox bookmarks file, and parsing
    it into a tree of folders and bookmarks.
    """
    def __init__(self, bookmarks_file: str):
        """
        Opens the provided bookmarks file and loads in into a JSON object.

        :param bookmarks_file: a Firefox bookmarks file in JSON format
        """
        with open(bookmarks_file, "r") as fp:
            self._bookmarks_json: dict = json.load(fp)

    def construct_node_tree(self) -> Node:
        """
        Constructs a tree of nodes by travelling through the read bookmarks
        file. Depending on the JSON data, a node will either be a folder or a
        bookmark.

        :return: A node that acts as the root, with child nodes that
        corresponds to the whole bookmarks file.

        :raises InvalidBookmarksDictError: if the file read by this class isn't
        a valid Firefox bookmarks file.
        """
        type_code = self._bookmarks_json.get("typeCode")
        if type_code is None or type_code != 2:
            raise InvalidBookmarksDictError("The root node must be a folder.")

        children = self._bookmarks_json.get("children")
        if children is None or not type(children) is list:
            raise InvalidBookmarksDictError("The root node must have children.")

        return Node("", "", 1)
