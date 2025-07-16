"""Module to write lobster configuration file.

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

from io import TextIOWrapper

from lobster_doxygen.lobster_item import LobsterItem
from lobster_doxygen.lobster_kind import LobsterKind
from lobster_doxygen.utils import indent

# Variables ********************************************************************

# Classes **********************************************************************

# Functions ********************************************************************


def _write_with_indent(output_file: TextIOWrapper, level: int, text: str) -> None:
    """Write the given text to the output file with indentation.

    Args:
        output_file (TextIOWrapper): The output file to write the results to.
        level (int): The indentation level.
        text (str): The text to be written.
    """
    output_file.write(indent(level, text))


def _write_lobster_header(output_file: TextIOWrapper) -> None:
    """Write the header of the lobster configuration file.

    Args:
        output_file (TextIOWrapper): The output file to write the results to.
    """
    _write_with_indent(output_file, 0, "{\n")
    _write_with_indent(output_file, 1, '"data": [\n')


def _write_lobster_tail(output_file: TextIOWrapper) -> None:
    """Write the tail of the lobster configuration file.
    This function finalizes the lobster configuration file by closing the data array
    and adding metadata about the generator and schema.

    Args:
        output_file (TextIOWrapper): The output file to write the results to.
    """
    _write_with_indent(output_file, 1, "],\n")
    _write_with_indent(output_file, 1, '"generator": "doxygen2lobster",\n')
    _write_with_indent(output_file, 1, '"schema": "lobster-imp-trace",\n')
    _write_with_indent(output_file, 1, '"version": 3\n')
    _write_with_indent(output_file, 0, "}\n")


def _write_lobster_item(output_file: TextIOWrapper, lobster_item: LobsterItem) -> None:
    """Write a lobster item to the output file.

    Args:
        output_file (TextIOWrapper): The output file to write the results to.
        lobster_item (LobsterItem): The lobster item to be written.
    """
    line = "null"
    column = "null"

    if lobster_item.line is not None:
        line = lobster_item.line

    if lobster_item.column is not None:
        column = lobster_item.column

    _write_with_indent(output_file, 2, "{\n")
    _write_with_indent(output_file, 3, f'"tag": "{lobster_item.get_tag()}",\n')
    _write_with_indent(output_file, 3, '"location": {\n')
    _write_with_indent(output_file, 4, '"kind": "file",\n')
    _write_with_indent(output_file, 4, f'"file": "{lobster_item.file_name}",\n')
    _write_with_indent(output_file, 4, f'"line": {line},\n')
    _write_with_indent(output_file, 4, f'"column": {column}\n')
    _write_with_indent(output_file, 3, "},\n")
    _write_with_indent(output_file, 3, f'"name": "{lobster_item.name}",\n')
    _write_with_indent(output_file, 3, '"messages": [],\n')

    if 0 == len(lobster_item.just_up):
        _write_with_indent(output_file, 3, '"just_up": [],\n')
    else:
        _write_with_indent(output_file, 3, '"just_up": [\n')

        for idx, just_up in enumerate(lobster_item.just_up):
            if 0 < idx:
                output_file.write(",\n")
            _write_with_indent(output_file, 4, f'"{just_up}"')

        output_file.write("\n")
        _write_with_indent(output_file, 3, "],\n")

    _write_with_indent(output_file, 3, '"just_down": [],\n')
    _write_with_indent(output_file, 3, '"just_global": [],\n')

    if 0 == len(lobster_item.refs):
        _write_with_indent(output_file, 3, '"refs": [],\n')
    else:
        _write_with_indent(output_file, 3, '"refs": [\n')

        for idx, ref in enumerate(lobster_item.refs):
            if 0 < idx:
                output_file.write(",\n")
            _write_with_indent(output_file, 4, f'"req {ref}"')

        output_file.write("\n")
        _write_with_indent(output_file, 3, "],\n")

    _write_with_indent(output_file, 3, f'"language": "{lobster_item.language}",\n')
    _write_with_indent(output_file, 3, f'"kind": "{lobster_item.kind.value}"\n')
    _write_with_indent(output_file, 2, "}")


def write_lobster_config(file_name: str, lobster_items: list[LobsterItem]) -> None:
    """Write the lobster configuration file.

    Args:
        file_name (str): The name of the file.
        lobster_items (List[LobsterItem]): The list of lobster items.
    """
    cnt = 0

    container_kind = [LobsterKind.CLASS, LobsterKind.STRUCT, LobsterKind.INTERFACE, LobsterKind.NAMESPACE]

    with open(file_name, "w", encoding="utf-8") as output_file:
        _write_lobster_header(output_file)

        for lobster_item in lobster_items:
            skip = False

            # Skip container items with childs and without references or justifications.
            if lobster_item.kind in container_kind:
                if lobster_item.has_children() is True:
                    if (lobster_item.has_refs() is False) and (lobster_item.has_just_up() is False):
                        skip = True

            # Skip file items in general.
            elif lobster_item.kind == LobsterKind.FILE:
                skip = True

            # If not skipped, write the lobster item to the output file.
            if skip is False:
                if 0 < cnt:
                    output_file.write(",\n")

                _write_lobster_item(output_file, lobster_item)
                cnt += 1

            # If the container item has child items, write them to the output file.
            else:
                for lobster_item_child in lobster_item.get_children():
                    if 0 < cnt:
                        output_file.write(",\n")

                    _write_lobster_item(output_file, lobster_item_child)
                    cnt += 1

        output_file.write("\n")
        _write_lobster_tail(output_file)


# Main *************************************************************************
