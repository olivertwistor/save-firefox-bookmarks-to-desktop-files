from bookmarks2desktop.tree.node import Node


class Bookmark(Node):
    def __init__(self, guid: str, title: str, uri: str):
        super().__init__(guid, title, 1)
        self._uri = uri
