"""Source code for logging. Extends Python's standard logging."""
import logging
import os.path
import sys
from datetime import datetime


class ShortPathnameFormatter(logging.Formatter):
	"""Formatter for the logging system. Introduces 'short_pathname', a new format tag that works like 'pathname', but
	only includes the path from src/."""

	def __init__(self) -> None:
		super().__init__("%(asctime)s %(levelname)s - %(message)s [%(short_pathname)s:%(lineno)d]", "%Y-%m-%d %H:%M:%S")

	def format(self, record: logging.LogRecord) -> str:
		if "pathname" in record.__dict__.keys():
			split_token = f"src{os.path.sep}"
			path_splits = record.pathname.split(split_token)
			record.short_pathname = path_splits[-1]
		return super().format(record)


class Logger(logging.Logger):
	"""Writes logs to stderr and the file system."""

	def __init__(self, name: str, level: int = logging.NOTSET) -> None:
		"""
		Initialises Python's own logging as a foundation, and adds two log handlers: one writes to stderr and one
		writes to the file system.

		:param name: Name of the logger. Should be '__name__'.
		:param level: On which lowest level this logger activates. Default is logging.NOTSET.
		"""
		super().__init__(name, level)
		self.addHandler(get_stream_handler(logging.DEBUG))
		# self.addHandler(get_file_handler(logging.DEBUG))
		pass


def get_stream_handler(logging_level: int) -> logging.StreamHandler:
	"""Creates a log handler, activated at the 'logging_level', that writes to stderr."""
	handler = logging.StreamHandler(sys.stderr)
	handler.setLevel(logging_level)
	handler.setFormatter(ShortPathnameFormatter())
	return handler


def get_file_handler(logging_level: int) -> logging.FileHandler:
	"""Creates a log handler, activated at the 'logging_level', that writes to the file system."""
	today = datetime.now().strftime("%Y-%m-%d")
	file_path = os.path.join(os.getcwd(), f"{today}.log")
	handler = logging.FileHandler(file_path, "a", "utf-8")
	handler.setLevel(logging_level)
	handler.setFormatter(ShortPathnameFormatter())
	return handler
