"""Module with script error codes.

Author: Dominik Knoll (dominik.knoll@newtec.de)
"""

# lobster-doxygen - Doxygen XML to LOBSTER common interchange format converter
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Imports **********************************************************************

from enum import IntEnum

# Variables ********************************************************************

# Classes **********************************************************************


class Ret(IntEnum):
    """The Error codes of lobster-doxygen tool."""

    RET_OK = 0
    RET_ERROR = 1
    RET_ERROR_ARGPARSE = 2  # Must be 2 to match the argparse error code.
    RET_ERROR_FILEPATH_INVALID = 3
    RET_ERROR_NO_LOBSTER_ITEMS = 4


# Functions ********************************************************************

# Main *************************************************************************
