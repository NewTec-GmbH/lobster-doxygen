"""Module to check lobster items for rules.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# lobster-doxygen - Doxygen XML to LOBSTER common interchange format converter
# Copyright (c) NewTec GmbH 2025 - 2026   -   www.newtec.de
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

import logging

from lobster_doxygen.lobster_item import LobsterItem
from lobster_doxygen.lobster_kind import LobsterKind

# Variables ********************************************************************

LOG: logging.Logger = logging.getLogger(__name__)

# Classes **********************************************************************

# Functions ********************************************************************


def rule_check(lobster_items: list[LobsterItem]) -> bool:
    """Check the lobster items for rules.

    Args:
        lobster_items (list[LobsterItem]): The list of lobster items.

    Returns:
        bool: True if the rules are satisfied, False otherwise.
    """
    # lobster-trace: SwRequirements.sw_req_rule_file
    # lobster-trace: SwRequirements.sw_req_rule_class
    success = True

    for lobster_item in lobster_items:
        # Its not allowed to have requirements and justifications on file level.
        if lobster_item.kind == LobsterKind.FILE:
            if lobster_item.has_refs() or lobster_item.has_just_up():
                LOG.error("The %s '%s' has requirements or justifications on file level.",
                          lobster_item.kind.value, lobster_item.name)
                success = False

        if success is True:
            # Its not allowed to have a lobster item parent with requirements and
            # any child item with requirements.
            if lobster_item.has_refs() or lobster_item.has_just_up():
                for lobster_item_child in lobster_item.get_children():
                    if lobster_item_child.has_refs():
                        LOG.error("The %s '%s' has child item '%s' with requirements.",
                                  lobster_item.kind.value, lobster_item.name,
                                  lobster_item_child.name)
                        success = False
                    elif lobster_item_child.has_just_up():
                        LOG.error("The %s '%s' has child item '%s' with justification.",
                                  lobster_item.kind.value, lobster_item.name,
                                  lobster_item_child.name)
                        success = False

                    if success is False:
                        break

        if success is False:
            break

    return success


# Main *************************************************************************
