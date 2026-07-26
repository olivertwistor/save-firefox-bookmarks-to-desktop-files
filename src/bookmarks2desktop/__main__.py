"""
This is the main script of this app. It contains the main program flow.
"""
import argparse
import datetime
import logging


def setup_logging() -> None:
	"""
	Setups logging with the correct format and redirects the output to stderr.
	"""
	timestamp = datetime.datetime.now()
	today = timestamp.strftime("%Y-%m-%d")

	logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s",
			datefmt="%Y-%m-%d %H:%M:%S",
			level=logging.DEBUG)


def read_console_parameters() -> tuple:
	"""
	Reads the console parameters passed to this app.

	:return: A tuple containing the source file and a flag for whether to
	overwrite any files
	"""
	parser = argparse.ArgumentParser(prog="bookmarks2desktop", description="Extracts Firefox bookmarks "
	                                                                       "to .desktop files.")
	parser.add_argument("source_file", help="path to an exported Firefox bookmarks file "
	                                        "(JSON-formatted)")
	parser.add_argument("-o",
			"--overwrite",
			action="store_true",
			default=False,
			help="overwrite files if the target path for a "
			     "bookmark file already exists on the filesystem")

	args = parser.parse_args()

	return args.source_file, args.overwrite


if __name__ == "__main__":
	setup_logging()
	source_file, overwrite_files = read_console_parameters()
