"""Setup script for mp3p"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="mp3p",
    version="1.0.0",
    description="Play mp3 files over the commandline",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/josiah-bennett/mp3p",
    author="Josiah Bennett",
    author_email="josiah.bennett@web.de",
    license="GNU GPLv3",
    packages=["mp3p"],
    include_package_data=True,
    install_requires=[
        "python-vlc"
    ],
    entry_points={"console_scripts": ["mp3p=mp3p.__main__:main"]},
)
