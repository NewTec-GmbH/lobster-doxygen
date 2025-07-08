"""Module to parse index.xml file.

Module that parse doxygen index.xml file and returns list with LobsterItems.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

import doxmlparser
from doxmlparser.compound import DoxCompoundKind, DoxMemberKind, compounddefType, sectiondefType, descriptionType

from lobster_doxygen.lobster_item import LobsterItem
from lobster_doxygen.lobster_kind import LobsterKind
from lobster_doxygen.printer import Printer
from lobster_doxygen.indent import indent


# Variables ********************************************************************

LOG = Printer()

# Classes **********************************************************************

# Functions ********************************************************************


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
            LOG.print_info(indent(3, f"Requirement: {req_id}"))

        # Is it a justification?
        elif value.startswith("Justification: "):
            just_up_id = value[15:]
            just_up.append(just_up_id)
            LOG.print_info(indent(3, f"Justification: {just_up_id}"))

    lobster_item.refs.extend(refs)
    lobster_item.just_up.extend(just_up)


def _parse_detail_description(lobster_item: LobsterItem, detailed_description: descriptionType) -> None:
    """Parse the detailed description and process it.

    Args:
        lobster_item (LobsterItem): The lobster item to be filled.
        detaileddescription (descriptionType): The detailed description to be parsed.
    """
    for para in detailed_description.get_para():
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

        LOG.print_info(indent(2, f"member: {memberdef.get_name()}"))
        LOG.print_info(indent(3, f"kind: {memberdef.get_kind()}"))

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


def _parse_compound(path: str, base_name: str) -> list[LobsterItem]:
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

        LOG.print_info(f"compound: {compounddef.get_compoundname()}")
        LOG.print_info(indent(1, f"kind: {kind}"))

        lobster_item.language = compounddef.get_language()
        lobster_item.name = compounddef.get_compoundname()
        lobster_item.file_name = compounddef.get_location().get_file()
        lobster_item.line = compounddef.get_location().get_line()
        lobster_item.column = compounddef.get_location().get_column()

        _parse_detail_description(lobster_item, compounddef.get_detaileddescription())
        _parse_sections(lobster_item, compounddef)

        lobster_items.append(lobster_item)

    return lobster_items


def parse_index(path: str) -> list[LobsterItem]:
    """Parse the index file, process each compound defined in it and build
        the lobster items.

    Args:
        path (str): The directory name where the index file is located.

    Returns:
        list[LobsterItem]: The list of lobster items.
    """
    lobster_items = []
    root_obj = doxmlparser.index.parse(path + "/index.xml", True)

    for compound in root_obj.get_compound():  # for each compound defined in the index
        lobster_items.extend(_parse_compound(path, compound.get_refid()))

    return lobster_items
