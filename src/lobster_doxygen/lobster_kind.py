"""Module to represent the kind of lobster item.

Author: Andreas Merkle (andreas.merkle@newtec.de)
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

import enum

# Variables ********************************************************************

# Classes **********************************************************************


class LobsterKind(enum.Enum):
    """Enum to represent the kind of lobster item."""

    UNDEFINED = "Undefined"
    FUNCTION = "Function"
    PROTOTYPE = "Prototype"
    METHOD = "Method"
    CLASS = "Class"
    STRUCT = "Struct"
    INTERFACE = "Interface"
    FILE = "File"
    NAMESPACE = "Namespace"


# Functions ********************************************************************

# Main *************************************************************************
