"""Module set indent to string.

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

# Variables ********************************************************************

_INDENT_SPACES = 4

# Classes **********************************************************************

# Functions ********************************************************************


def indent(level: int, text: str) -> str:
    """Indent the given text with the specified level.

    Args:
        level (int): The indentation level.
        text (str): The text to be indented.

    Returns:
        str: The indented text.
    """
    return " " * (_INDENT_SPACES * level) + text


# Main *************************************************************************
