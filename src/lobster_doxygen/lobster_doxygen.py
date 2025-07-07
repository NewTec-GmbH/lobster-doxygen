"""Script to generate the lobster common interchange format from a doxygen XML output.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

import logging
import sys
import argparse
import enum
from typing import List
from io import TextIOWrapper
import doxmlparser
from doxmlparser.compound import DoxCompoundKind, DoxMemberKind, compounddefType, sectiondefType, descriptionType

try:
    from lobster_doxygen.version import __version__, __author__, __email__, __repository__, __license__
except ModuleNotFoundError:
    # provide dummy information when not installed as package but called directly
    # also necessary to get sphinx running without error
    __version__ = "dev"
    __author__ = "Andreas Merkle"
    __email__ = "andreas.merkle@newtec.de"
    __repository__ = "https://github.com/NewTec-GmbH/lobster-doxygen.git"
    __license__ = "GPLv3"

# Variables ********************************************************************

LOG: logging.Logger = logging.getLogger(__name__)
# Indentation for the lobster configuration file.

_INDENT_SPACES = 4

# Verbose mode flag.
_VERBOSE_MODE = False

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


def _indent(level: int, text: str) -> str:
    """Indent the given text with the specified level.

    Args:
        level (int): The indentation level.
        text (str): The text to be indented.

    Returns:
        str: The indented text.
    """
    return " " * (_INDENT_SPACES * level) + text


def _print_verbose(text: str) -> None:
    """Print the given text only if verbose mode is enabled.

    Args:
        text (str): The text to be printed.
    """
    if _VERBOSE_MODE:
        print(text)


def _parse_xrefdescription(lobster_item: LobsterItem, xrefdescription: descriptionType) -> None:
    """Parse the xrefdescription to retrieve references and add them to the lobster item.

    Args:
        lobster_item (LobsterItem): The lobster item to be filled.
        xrefdescription (descriptionType): The xrefdescription to be parsed.
    """
    refs = []
    just_up = []

    for para in xrefdescription.get_para():
        value = para.get_valueOf_().strip()

        # Is it a requirement reference?
        if value.startswith("Requirement: "):
            req_id = value[13:]
            refs.append(req_id)
            _print_verbose(_indent(3, f"Requirement: {req_id}"))

        # Is it a justification?
        elif value.startswith("Justification: "):
            just_up_id = value[15:]
            just_up.append(just_up_id)
            _print_verbose(_indent(3, f"Justification: {just_up_id}"))

    lobster_item.refs.extend(refs)
    lobster_item.just_up.extend(just_up)


def _parse_detail_description(lobster_item: LobsterItem, detaileddescription: descriptionType) -> None:
    """Parse the detailed description and process it.

    Args:
        lobster_item (LobsterItem): The lobster item to be filled.
        detaileddescription (descriptionType): The detailed description to be parsed.
    """
    for para in detaileddescription.get_para():
        for xrefsect in para.get_xrefsect():
            _parse_xrefdescription(lobster_item, xrefsect.get_xrefdescription())


def _parse_members(lobster_item: LobsterItem, compounddef: compounddefType, sectiondef: sectiondefType) -> None:
    """Parse the members of the compound definition and process them.

    Args:
        lobster_item (LobsterItem): The lobster item to be filled.
        compounddef (compounddefType): The compound definition to be parsed.
        sectiondef (sectiondefType): The section definition to be parsed.
    """

    function_like_kind = [DoxMemberKind.FUNCTION, DoxMemberKind.PROTOTYPE]

    for memberdef in sectiondef.get_memberdef():
        lobster_item_child = None
        lobster_item_namespace = None
        lobster_item_id = memberdef.get_id()

        if compounddef.get_kind() in [DoxCompoundKind.CLASS, DoxCompoundKind.STRUCT, DoxCompoundKind.INTERFACE]:

            if memberdef.get_kind() in function_like_kind:
                # Process function-like members
                lobster_item_child = LobsterItem(lobster_item_id)
                lobster_item_child.kind = LobsterKind.METHOD
                lobster_item_namespace = compounddef.get_compoundname()
            else:
                # Skip other member kinds
                continue

        elif compounddef.get_kind() in [DoxCompoundKind.FILE, DoxCompoundKind.NAMESPACE]:
            if memberdef.get_kind() in function_like_kind:
                # Process function-like members
                lobster_item_child = LobsterItem(lobster_item_id)
                lobster_item_child.kind = LobsterKind.FUNCTION
            else:
                # Skip other member kinds
                continue

        _print_verbose(_indent(2, f"member: {memberdef.get_name()}"))
        _print_verbose(_indent(3, f"kind: {memberdef.get_kind()}"))

        lobster_item_child.language = compounddef.get_language()

        if lobster_item_namespace is not None:
            lobster_item_child.name = lobster_item_namespace
            lobster_item_child.name += "."

        lobster_item_child.name += memberdef.get_name()
        lobster_item_child.file_name = memberdef.get_location().get_file()
        lobster_item_child.line = memberdef.get_location().get_line()
        lobster_item_child.column = memberdef.get_location().get_column()

        _parse_detail_description(lobster_item_child, memberdef.get_detaileddescription())

        lobster_item.append_lobster_child(lobster_item_child)


def _parse_sections(lobster_item: LobsterItem, compounddef: compounddefType) -> None:
    """Parse the sections of the compound definition and process them.

    Args:
        lobster_item (LobsterItem): The lobster item to be filled.
        compounddef (compounddefType): The compound definition to be parsed.
    """

    for sectiondef in compounddef.get_sectiondef():
        _parse_members(lobster_item, compounddef, sectiondef)


def _parse_compound(path: str, base_name: str) -> List[LobsterItem]:
    """Parse the compound file and process it.

    Args:
        path (str): The directory name where the compound file is located.
        base_name (str): The base name of the compound file to be parsed.

    Returns:
        List[LobsterItem]: The list of lobster items.
    """
    lobster_items = []
    root_obj = doxmlparser.compound.parse(path + "/" + base_name + ".xml", True)

    for compounddef in root_obj.get_compounddef():
        lobster_item = None
        kind = compounddef.get_kind()
        lobster_item_id = compounddef.get_id()

        if DoxCompoundKind.CLASS == kind:
            lobster_item = LobsterItem(lobster_item_id)
            lobster_item.kind = LobsterKind.CLASS

        elif DoxCompoundKind.STRUCT == kind:
            lobster_item = LobsterItem(lobster_item_id)
            lobster_item.kind = LobsterKind.STRUCT

        elif DoxCompoundKind.INTERFACE == kind:
            lobster_item = LobsterItem(lobster_item_id)
            lobster_item.kind = LobsterKind.INTERFACE

        elif DoxCompoundKind.FILE == kind:
            lobster_item = LobsterItem(lobster_item_id)
            lobster_item.kind = LobsterKind.FILE

        elif DoxCompoundKind.NAMESPACE == kind:
            lobster_item = LobsterItem(lobster_item_id)
            lobster_item.kind = LobsterKind.NAMESPACE

        else:
            # Skip other compound kinds
            continue

        _print_verbose(f"compound: {compounddef.get_compoundname()}")
        _print_verbose(_indent(1, f"kind: {kind}"))

        lobster_item.language = compounddef.get_language()
        lobster_item.name = compounddef.get_compoundname()
        lobster_item.file_name = compounddef.get_location().get_file()
        lobster_item.line = compounddef.get_location().get_line()
        lobster_item.column = compounddef.get_location().get_column()

        _parse_detail_description(lobster_item, compounddef.get_detaileddescription())
        _parse_sections(lobster_item, compounddef)

        lobster_items.append(lobster_item)

    return lobster_items


def _parse_index(path: str) -> List[LobsterItem]:
    """Parse the index file, process each compound defined in it and build
        the lobster items.

    Args:
        path (str): The directory name where the index file is located.

    Returns:
        List[LobsterItem]: The list of lobster items.
    """
    lobster_items = []
    root_obj = doxmlparser.index.parse(path + "/index.xml", True)

    for compound in root_obj.get_compound():  # for each compound defined in the index
        lobster_items.extend(_parse_compound(path, compound.get_refid()))

    return lobster_items


def _write_with_indent(output_file: TextIOWrapper, level: int, text: str) -> None:
    """Write the given text to the output file with indentation.

    Args:
        output_file (TextIOWrapper): The output file to write the results to.
        level (int): The indentation level.
        text (str): The text to be written.
    """
    output_file.write(_indent(level, text))


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


def _write_lobster_config(file_name: str, lobster_items: List[LobsterItem]) -> None:
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


def rule_check(lobster_items: List[LobsterItem]) -> bool:
    """Check the lobster items for rules.

    Args:
        lobster_items (List[LobsterItem]): The list of lobster items.

    Returns:
        bool: True if the rules are satisfied, False otherwise.
    """
    success = True

    for lobster_item in lobster_items:
        # Its not allowed to have requirements and justifications on file level.
        if lobster_item.kind == LobsterKind.FILE:
            if lobster_item.has_refs() or lobster_item.has_just_up():
                print(
                    f"Error: The {lobster_item.kind.value} '{lobster_item.name}' "
                    f"has requirements or justifications on file level."
                )
                success = False

        if success is True:
            # Its not allowed to have a lobster item parent with requirements and
            # any child item with requirements.
            if lobster_item.has_refs() or lobster_item.has_just_up():
                for lobster_item_child in lobster_item.get_children():
                    if lobster_item_child.has_refs():
                        print(
                            f"Error: The {lobster_item.kind.value} '{lobster_item.name}' "
                            f"has child item '{lobster_item_child.name}' with requirements."
                        )
                        success = False
                    elif lobster_item_child.has_just_up():
                        print(
                            f"Error: The {lobster_item.kind.value} '{lobster_item.name}' "
                            f"has child item '{lobster_item_child.name}' with justification."
                        )
                        success = False

                    if success is False:
                        break

        if success is False:
            break

    return success


def main() -> int:
    """Main function to convert doxygen XML output to lobster common interchange format.

    Returns:
        int: 0 on success, 1 on failure.
    """
    status = 1

    # Create argument parser which accepts one mandatory parameter for the doxygen
    # folder that contains the XML output.
    parser = argparse.ArgumentParser(description="Convert doxygen XML output to lobster common interchange format.")
    parser.add_argument("doxygen_folder", type=str, help="Path to the doxygen XML output folder.")
    parser.add_argument("-o", "--output", type=str, help="Output file name.", default="lobster.cfg")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    # Parse the command line arguments.
    args = parser.parse_args()

    # Is verbose mode enabled?
    if args.verbose:
        global _VERBOSE_MODE  # pylint: disable=global-statement
        _VERBOSE_MODE = True

    # Check if the doxygen folder exists.
    if args.doxygen_folder:

        lobster_items = _parse_index(args.doxygen_folder)

        if rule_check(lobster_items) is True:
            _write_lobster_config(args.output, lobster_items)
            status = 0

    return status


# Main *************************************************************************


if __name__ == "__main__":
    sys.exit(main())
