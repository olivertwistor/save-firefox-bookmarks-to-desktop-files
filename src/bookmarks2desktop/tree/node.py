from src.bookmarks2desktop.exceptions import InvalidBookmarksDictError


class Node:
	"""
	This class represents a node, the common denominator between bookmarks and
	folders.
	"""

	def __init__(self, guid: str, title: str, type_code: int):
		self._guid = guid
		self._title = title
		self._type_code = type_code

	@classmethod
	def from_dict(cls, node_dict: dict) -> 'Node':
		"""
		Creates a new node based on the provided dict. That dict must at least
		contain the following keys: guid, title and typeCode.

		:param node_dict: a dict containing data needed for a node

		:return: The created node.

		:raises InvalidBookmarksDictError: if the provided dict isn't from a
		valid Firefox bookmarks file.
		"""
		guid = node_dict.get("guid")
		title = node_dict.get("title")
		type_code = node_dict.get("typeCode")
		if guid is None or title is None or type_code is None:
			raise InvalidBookmarksDictError("The provided dict must contain a "
			                                "guid, title and typeCode.")

		return cls(guid, title, type_code)

	@property
	def name(self) -> str:
		"""
		Returns the name, which is a concatenation of the title and guid.

		:return: Concatenation of title and guid.
		"""
		return f"{self._title}_{self._guid}"
