import unittest

from bookmarks2desktop import parser


class TestJsonParser(unittest.TestCase):
    """
    Unit tests for the JsonParser class.
    """

    def setUp(self) -> None:
        """
        Parses two test bookmarks files: one proper Firefox bookmark file, one proper dict but not a Firefox bookmark file.
        """
        self.bookmarks = parser.parse_json("bookmarks.json")
        self.json_dict = parser.parse_json("json_dict.json")
