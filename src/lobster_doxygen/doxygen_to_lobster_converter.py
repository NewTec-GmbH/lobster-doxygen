"""lobster-doxygen main module.

Tool to generate LOBSTER common interchange format file from a doxygen XML output.

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
import os

from lobster_doxygen.ret import Ret
from lobster_doxygen.printer import Printer
from lobster_doxygen.get_lobster_items_from_doxygen_xml_folder import get_lobster_items_from_doxygen_xml_folder
from lobster_doxygen.write_lobster_common_interchange_format_file import write_lobster_common_interchange_format_file
from lobster_doxygen.rule_check import rule_check

# Variables ********************************************************************
LOG = Printer()

# Classes **********************************************************************


# Functions ********************************************************************


def convert_doxygen_xml_to_lobster_common_interchange_format(doxygen_xml_folder: str, output_file_name: str) -> Ret:
    # lobster-trace: SwRequirements.sw_req_cli_doxygen_xml_folder
    # lobster-trace: SwRequirements.sw_req_output_file_format
    # lobster-trace: SwRequirements.sw_req_cli_output
    # lobster-trace: SwRequirements.sw_req_no_trace
    """Convert xml files in doxygen_xml_folder to LOBSTER common interchange format file with name
    output.

    Args:
        doxygen_xml_folder (str): The Doxygen XML output directory, where the file index.xml is located.
        output_file_name (str): Path and file name for LOBSTER common interchange format file.

    Return:
        Ret.RET_OK: LOBSTER common interchange format file successful created.
        Ret.RET_ERROR_FILEPATH_INVALID: No index.xml file in doxygen_folder
        Ret.RET_ERROR: Conversion not successful.
    """
    ret_status = Ret.RET_ERROR
    is_index_file_found = False

    if not os.path.isfile(doxygen_xml_folder + "/index.xml"):
        LOG.print_error(
            f"No doxygen index.xml file in doxygen_xml_folder {doxygen_xml_folder}.")
        ret_status = Ret.RET_ERROR_FILEPATH_INVALID
        is_index_file_found = False
    else:
        is_index_file_found = True

    if is_index_file_found:
        lobster_items = get_lobster_items_from_doxygen_xml_folder(doxygen_xml_folder)
        # Continue only if no error during parsing.
        if lobster_items is not None:
            # Check if lobster items are found.
            if 0 == len(lobster_items):
                LOG.print_warning("No lobster items found in the doxygen XML output.")

            if rule_check(lobster_items) is True:
                write_lobster_common_interchange_format_file(lobster_items, output_file_name)
                ret_status = Ret.RET_OK

    return ret_status
