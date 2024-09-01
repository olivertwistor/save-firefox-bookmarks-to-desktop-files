from bookmarks2desktop.tree.node import Node


class Folder(Node):
    def __init__(self, guid: str, title: str):
        super().__init__(guid, title, 1)
        self._children = []

    def add_child(self, node: Node) -> None:
        """
        Adds a child node to this folder.

        :param node: the node to add; can either be another folder or a bookmark
        """
        self._children.append(node)
