"""This module provides version and author information."""

#*******************************************************************************
# Copyright (c) NewTec GmbH 2024   -   www.newtec.de
#*******************************************************************************

# Imports **********************************************************************
import importlib.metadata as meta
import os
import sys
import toml

# Variables ********************************************************************

__version__ = "???"
__author__ = "???"
__email__ = "???"
__repository__ = "???"
__license__ = "???"

# Classes **********************************************************************

# Functions ********************************************************************


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # pylint: disable=protected-access
        # pylint: disable=no-member
        base_path = sys._MEIPASS
    except Exception:  # pylint: disable=broad-except
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def init_from_metadata():
    """Initialize dunders from importlib.metadata
    Requires that the package was installed.

    Returns:
        list: Tool related information
    """

    my_metadata = meta.metadata('template_python')

    return \
        my_metadata['Version'], \
        my_metadata['Author'], \
        my_metadata['Author-email'], \
        my_metadata['Project-URL'].replace("repository, ", ""), \
        my_metadata['License']


def init_from_toml():
    """Initialize dunders from pypackage.toml file

    Tried if package wasn't installed.

    Returns:
        list: Tool related information
    """

    toml_file = resource_path("pyproject.toml")
    data = toml.load(toml_file)

    return \
        data["project"]["version"], \
        data["project"]["authors"][0]["name"], \
        data["project"]["authors"][0]["email"], \
        data["project"]["urls"]["repository"], \
        data["project"]["license"]["text"]

# Main *************************************************************************


try:
    __version__, __author__, __email__, __repository__, __license__ = init_from_metadata()

except meta.PackageNotFoundError:
    __version__, __author__, __email__, __repository__, __license__ = init_from_toml()
