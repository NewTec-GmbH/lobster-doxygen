"""Module with script error codes.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# lobster-doxygen
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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


# Functions ********************************************************************
