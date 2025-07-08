"""Module with script error codes.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************
from enum import IntEnum
from dataclasses import dataclass

# Variables ********************************************************************

# Classes **********************************************************************


@dataclass
class Ret:
    """The Error codes of lobster-doxygen tool."""

    class CODE(IntEnum):
        """The exit statuses of the modules."""

        RET_OK = 0
        RET_ERROR = 1
        RET_ERROR_ARGPARSE = 2  # Must be 2 to match the argparse error code.
        RET_ERROR_FILEPATH_INVALID = 3

    MSG = {
        CODE.RET_OK: "Process successful.",
        CODE.RET_ERROR: "Error occurred.",
        CODE.RET_ERROR_ARGPARSE: "Error while parsing arguments.",
        CODE.RET_ERROR_FILEPATH_INVALID: "The provided filepath does not exist.",
    }


@dataclass
class Warnings:
    """The messages corresponding to the return values and warnings."""

    class CODE(IntEnum):
        """Th Warnings of the modules."""

        None

    MSG = {}


# Functions ********************************************************************
