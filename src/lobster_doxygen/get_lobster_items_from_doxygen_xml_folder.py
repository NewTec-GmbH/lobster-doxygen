"""Module to parse index.xml file.

Module that parse doxygen index.xml file and returns list with LobsterItems.

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

import doxmlparser
from doxmlparser.compound import DoxCompoundKind, DoxMemberKind, compounddefType, descriptionType

from lobster_doxygen.lobster_item import LobsterItem
from lobster_doxygen.lobster_kind import LobsterKind
from lobster_doxygen.printer import Printer
from lobster_doxygen.utils import indent


# Variables ********************************************************************

LOG = Printer()

# Requirement specifier, which is configured in the doxygen configuration, see alias.
_REQ_SPECIFIER = "Requirement"

# Justification specifier, which is configured in the doxygen configuration, see alias.
_JUSTIFICATION_SPECIFIER = "Justification"

# List for DoxCompoundKinds that are converted to a LobsterItems, others kinds are skipped.
_LOBSTER_ITEM_KINDS = [
    DoxCompoundKind.CLASS,
    DoxCompoundKind.STRUCT,
    DoxCompoundKind.INTERFACE,
    DoxCompoundKind.FILE,
    DoxCompoundKind.NAMESPACE,
    DoxCompoundKind.GROUP,
]

# Classes **********************************************************************

# Functions ********************************************************************


def _get_xrefdescriptions_from_detaileddescription(detaileddescription: descriptionType) -> list[descriptionType]:
    """Get a list with xrefdescriptions from detaileddescription.

    Args:
        detaileddescription (descriptionType): The detaileddescription to be parsed
        for xrefdescriptions.

    Return:
        list[descriptionType]: List with xrefdescriptions.
    """
    xrefdescriptions = []

    for para in detaileddescription.get_para():
        for xrefsect in para.get_xrefsect():
            xrefdescription = xrefsect.get_xrefdescription()
            xrefdescriptions.append(xrefdescription)

    return xrefdescriptions


def _get_refs_and_just_up_from_detaileddescription(detaileddescription: descriptionType) -> tuple[list[str], list[str]]:
    """Parse the detaileddescription for xrefdescription to retrieve requirement
    with _REQ_SPECIFIER and justification with _JUSTIFICATION_SPECIFIER
    references and return them with two separate lists.

    Args:
        detaileddescription (descriptionType): The detaileddescription to be parsed
        for requirements and justifications.

    Returns:
        list[str], list[str]:
        List with requirements strings found in detaileddescription,
        List with justification strings found in detaileddescripiton
    """
    refs = []
    just_up = []

    xrefdescriptions = _get_xrefdescriptions_from_detaileddescription(detaileddescription)
    for xrefdescription in xrefdescriptions:
        for para in xrefdescription.get_para():
            value = para.get_valueOf_().strip()

            # Look for requirement reference
            if value.startswith(f"{_REQ_SPECIFIER}: "):
                req_id = value[13:]
                refs.append(req_id)
                LOG.print_info(indent(3, f"{_REQ_SPECIFIER}: {req_id}"))

            # Look for justification
            elif value.startswith(f"{_JUSTIFICATION_SPECIFIER}: "):
                just_up_id = value[15:]
                just_up.append(just_up_id)
                LOG.print_info(indent(3, f"{_JUSTIFICATION_SPECIFIER}: {just_up_id}"))

    return refs, just_up


def _get_lobster_item_children_from_compounddef(compounddef: compounddefType) -> list[LobsterItem]:
    """Parse the members of the compound definition and returns list of
    children LobsterItems.

    Args:
        compounddef (compounddefType): The compound definition to be parsed for children.

    Returns:
        list[LobsterItem]: List with LobsterItem children.

    """
    lobster_item_children = []
    function_like_kind = [DoxMemberKind.FUNCTION, DoxMemberKind.PROTOTYPE]

    for sectiondef in compounddef.get_sectiondef():
        for memberdef in sectiondef.get_memberdef():
            LOG.print_info(indent(2, f"member: {memberdef.get_name()}"))
            lobster_item_child = None

            if compounddef.get_kind() in [DoxCompoundKind.CLASS, DoxCompoundKind.STRUCT, DoxCompoundKind.INTERFACE]:
                if memberdef.get_kind() in function_like_kind:
                    # Process function-like members
                    lobster_item_child = LobsterItem(memberdef.get_id())
                    lobster_item_child.kind = LobsterKind.METHOD
                    lobster_item_child.name = f"{compounddef.get_compoundname()}."

            elif compounddef.get_kind() in [DoxCompoundKind.FILE, DoxCompoundKind.NAMESPACE, DoxCompoundKind.GROUP]:
                if memberdef.get_kind() in function_like_kind:
                    # Process function-like members
                    lobster_item_child = LobsterItem(memberdef.get_id())
                    lobster_item_child.kind = LobsterKind.FUNCTION

            # Update only if LobsterItem was created
            if lobster_item_child is not None:
                LOG.print_info(indent(3, f"kind: {memberdef.get_kind()}"))

                lobster_item_child.language = compounddef.get_language()
                lobster_item_child.name += memberdef.get_name()
                lobster_item_child.file_name = memberdef.get_location().get_file()
                lobster_item_child.line = memberdef.get_location().get_line()
                lobster_item_child.column = memberdef.get_location().get_column()

                lobster_item_child.refs, lobster_item_child.just_up = _get_refs_and_just_up_from_detaileddescription(
                    memberdef.get_detaileddescription()
                )

                lobster_item_children.append(lobster_item_child)
            else:
                LOG.print_info(indent(3, f"kind: {memberdef.get_kind()} (skipped)"))

    return lobster_item_children


def _lobster_item_from_compounddef(compounddef: compounddefType) -> LobsterItem:
    """Creates a LobsterItem from comppunddef.

    Args:
        compounddef (compounddefType): The compound definition to be parsed
        for LobsterItem.

    Returns:
        LobsterItem: LobsterItem created from compounddef.
    """
    # lobster-trace: SwRequirements.sw_req_unspecified
    lobster_item = LobsterItem(compounddef.get_id())

    # DoxCompoundKind to LobsterKind
    lobster_item.kind = LobsterKind[compounddef.get_kind().upper()]

    lobster_item.language = compounddef.get_language()
    lobster_item.name = compounddef.get_compoundname()

    # A group has no location information on compounddef level.
    if compounddef.get_location() is None:
        lobster_item.file_name = ""
        lobster_item.line = 0
        lobster_item.column = 0
    else:
        lobster_item.file_name = compounddef.get_location().get_file()
        lobster_item.line = compounddef.get_location().get_line()
        lobster_item.column = compounddef.get_location().get_column()

    # Adds refs and just_up attributes
    lobster_item.refs, lobster_item.just_up = _get_refs_and_just_up_from_detaileddescription(
        compounddef.get_detaileddescription()
    )

    lobster_item_children = _get_lobster_item_children_from_compounddef(compounddef)
    for lobster_item_child in lobster_item_children:
        lobster_item.append_lobster_child(lobster_item_child)

    return lobster_item


def _get_lobster_items_from_compound(compound_path: str) -> list[LobsterItem]:
    """Parse the compound file and extract a list with LobsterItems inside file.

    Args:
        compound_path (str): The Path of the compound file to be parsed.

    Returns:
        list[LobsterItem]: The list of LobsterItems from compound.
    """
    # lobster-trace: SwRequirements.sw_req_file_level
    # lobster-trace: SwRequirements.sw_req_func_level
    # lobster-trace: SwRequirements.sw_req_type_level
    # lobster-trace: SwRequirements.sw_req_ns_level
    # lobster-trace: SwRequirements.sw_req_method_level
    # lobster-trace: SwRequirements.sw_req_interface_level
    lobster_items = []
    root_obj = doxmlparser.compound.parse(compound_path, True)

    for compounddef in root_obj.get_compounddef():
        LOG.print_info(f"compound: {compounddef.get_compoundname()}")

        kind = compounddef.get_kind()

        if kind in _LOBSTER_ITEM_KINDS:
            LOG.print_info(indent(1, f"kind: {kind}"))
            lobster_item = _lobster_item_from_compounddef(compounddef)
            lobster_items.append(lobster_item)
        else:
            LOG.print_info(indent(1, f"kind: {kind} (skipped)"))

    return lobster_items


def get_lobster_items_from_doxygen_xml_folder(doxygen_xml_folder: str) -> list[LobsterItem] | None:
    """Parse the doxygen XML index file, process each compound defined in it
    and build the LobsterItems list.

    Args:
        doxygen_xml_folder (str): The Doxygen XML output directory, where the
        file index.xml is located.

    Returns:
        list[LobsterItem] | None: The list of lobster items. If an error occurs,
        None is returned.
    """
    lobster_items = []

    try:
        # lobster-trace: SwRequirements.sw_req_input_root
        root_obj = doxmlparser.index.parse(doxygen_xml_folder + "/index.xml", True)

        for compound in root_obj.get_compound():  # for each compound defined in the index
            compound_path = doxygen_xml_folder + "/" + compound.get_refid() + ".xml"
            lobster_items.extend(_get_lobster_items_from_compound(compound_path))

    # pylint: disable=broad-exception-caught
    except Exception as e:
        LOG.print_error(f"{e}")
        lobster_items = None

    return lobster_items


# Main *************************************************************************
