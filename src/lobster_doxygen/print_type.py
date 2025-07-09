"""Module for print type.

The different print message types (error, warning, info).

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

# Variables ********************************************************************

# Classes **********************************************************************


class PrintType(IntEnum):
    """Different Printer Information Types."""

    ERROR = 0
    WARNING = 1
    INFO = 2


# Functions ********************************************************************
