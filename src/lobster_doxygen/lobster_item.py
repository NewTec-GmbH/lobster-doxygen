"""Module to represent a lobster item.

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

from typing import List

from lobster_doxygen.lobster_kind import LobsterKind

# Variables ********************************************************************

# Classes **********************************************************************


class LobsterItem:  # pylint: disable=too-many-instance-attributes
    """Class to represent a lobster item."""

    def __init__(self, item_id: str) -> None:
        """Initialize the lobster item.

        Args:
            item_id (str): The unique identifier of the lobster item.
        """
        self.item_id = item_id  # Unique identifier of the lobster item.
        self.file_name = ""  # Code location file name with path.
        self.line = None  # Code location line number.
        self.column = None  # Code location column number.
        self.name = ""  # Name shown in the trace report for this item.
        self.refs = []  # List of references to requirements.
        self.just_up = []  # List of justifications.
        self.language = ""  # Programming language of the code location.
        self.kind = LobsterKind.UNDEFINED  # Kind of the lobster item.
        self._children = []  # List of child items.

    def append_lobster_child(self, item: "LobsterItem") -> None:
        """Append an child to the lobster item.

        Args:
            item (LobsterItem): The item to append.
        """
        self._children.append(item)

    def get_children(self) -> List["LobsterItem"]:
        """Get the children of the lobster item.

        Returns:
            List[LobsterItem]: The list of child items.
        """
        return self._children

    def has_children(self) -> bool:
        """Check if the lobster item has children.

        Returns:
            bool: True if the lobster item has children, False otherwise.
        """
        return 0 < len(self._children)

    def has_refs(self) -> bool:
        """Check if the lobster item has references.

        Returns:
            bool: True if the lobster item has references, False otherwise.
        """
        return 0 < len(self.refs)

    def has_just_up(self) -> bool:
        """Check if the lobster item has justifications.

        Returns:
            bool: True if the lobster item has justifications, False otherwise.
        """
        return 0 < len(self.just_up)

    def _language_to_tag_prefix(self, language: str) -> str:
        """Convert the language to a tag prefix.

        Args:
            language (str): The language to be converted.

        Returns:
            str: The tag prefix for the given language.
        """
        prefix = "unknown "

        if language == "C":
            prefix = "c"
        elif language == "C++":
            prefix = "cpp"
        elif language == "C#":
            prefix = "cs"
        elif language == "Java":
            prefix = "java"
        elif language == "Python":
            prefix = "python"

        return prefix

    def get_tag(self) -> str:
        """Get the tag of the lobster item.

        Returns:
            str: The tag of the lobster item.
        """
        return self._language_to_tag_prefix(self.language) + " " + self.item_id


# Functions ********************************************************************
