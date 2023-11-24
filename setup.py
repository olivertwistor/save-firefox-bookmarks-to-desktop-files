"""
Setup for the Save Firefox Bookmarks To Desktop Files app.
"""
from setuptools import setup, find_packages


# Read README.md as the long description.
with open("README.md") as fp:
    readme = fp.read()

# READ LICENSE as the license.
with open("LICENSE") as fp:
    license_file = fp.read()

# Do the setup.
setup(
    name="olivertwistor.bookmarks2desktop",
    version="0.1.0",
    description="Saves Firefox bookmarks to .desktop files.",
    long_description=readme,
    author="Johan Nilsson",
    author_email="oliver_twistor@hotmail.com",
    url="https://github.com/olivertwistor/save-firefox-bookmarks-to-desktop-files",
    license=license_file,
    packages=find_packages(exclude=('tests', 'docs'))
)
