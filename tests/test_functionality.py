"""Test the program functionality.

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

import sys
from pathlib import Path
import json

from lobster_doxygen.__main__ import main

# Variables ********************************************************************

# LOBSTER output file that is created and deleted for tests.
TEST_LOBSTER_OUTPUT_FILE = "./tests/utils/output-test.json"

# Directory with Doxygen XML files.
TEST_XML_FOLDER = "./tests/utils/xml"

# Directory with Doxygen XML files from cpp-function-prototype project.
TEST_FUNCTION_PROTOTYPE_XML_FOLDER = "./tests/utils/cpp-function-prototype/out/xml"

# Directory with Doxygen XML files from cpp-struct-union-class project.
TEST_TYPE_XML_FOLDER = "./tests/utils/cpp-struct-union-class/out/xml"

# Empty directory with no XML files.
EMPTY_FOLDER = "./tests/utils/empty_folder"

# Classes **********************************************************************

# Functions ********************************************************************


def _delete_test_lobster_output_file() -> None:
    """Delete the LOBSTER file if it exists."""
    if Path(TEST_LOBSTER_OUTPUT_FILE).exists() and Path(TEST_LOBSTER_OUTPUT_FILE).is_file():
        Path(TEST_LOBSTER_OUTPUT_FILE).unlink()


def _get_data_items_from_lobster_file() -> dict:
    """
    Get dictionary of data section in TEST_LOBSTER_OUTPUT file.

    Returns:
        dict: Dictionary of data section.
    """
    with open(TEST_LOBSTER_OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data_items = data.get("data", [])
    return data_items


def _is_string_in_lobster_output_file_ref(search_string: str) -> bool:
    """
    Checks if search_string is TEST_LOBSTER_OUTPUT_FILE file in a data refs section.

    Args:
        search_string (str): Search string to lock for under refs.

    Returns:
        bool: True is search_string is found.
    """
    data_items = _get_data_items_from_lobster_file()
    refs = []
    for data_item in data_items:
        if data_item["refs"] != []:
            refs.extend(data_item["refs"])

    return search_string in refs


def _is_string_in_lobster_output_file_just_up(search_string: str) -> bool:
    """
    Checks if search_string is TEST_LOBSTER_OUTPUT_FILE file in a data just_up section.

    Args:
        search_string (str): Search string to lock for under just_up.

    Returns:
        bool: True is search_string is found.
    """
    data_items = _get_data_items_from_lobster_file()
    just_ups = []
    for data_item in data_items:
        if data_item["just_up"] != []:
            just_ups.extend(data_item["just_up"])

    return search_string in just_ups


def test_tc_input_root(record_property, capsys) -> None:
    # lobster-trace: SwTest.tc_input_root
    """
    Test calls program with doxygen_xml_folder path where a valid index.xml file is inside and
    checks that the program runs successfully.
    After that program is called with doxygen_xml_folder path where no index.xml file is inside
    and checks that the program returns an error.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_input_root")

    _test_program_with_valid_directory_to_index_file()
    _test_program_with_directory_with_no_index_file(capsys)


def _test_program_with_valid_directory_to_index_file() -> None:
    """
    Test calls program with doxygen_xml_folder path where a valid index.xml file is inside and
    checks that the program runs successfully.
    """

    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    exit_code = main()

    _delete_test_lobster_output_file()

    assert exit_code == 0, "Exit Code returns no success."


def _test_program_with_directory_with_no_index_file(capsys) -> None:
    """
    After that program is called with doxygen_xml_folder path where no index.xml file is inside
    and checks that the program returns an error.

    Args:
        capsys (Any): Used to capture stdout and stderr.
    """
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, EMPTY_FOLDER]

    exit_code = main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")
    assert exit_code != 0, "Exit Code returns success."
    assert error_output == ["Error: No doxygen index.xml file in doxygen_xml_folder ", f"{EMPTY_FOLDER}."]


def test_func_level(record_property) -> None:
    # lobster-trace: SwTest.tc_func_level
    """
    The test case calls the program with cpp-function-prototype XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_foo1" and "req SwRequirements.sw_req_foo" strings
    are found in the data items.
    The test also verifies that "foo2 justification" and "foo3 justification" strings are found in
    the just_up data items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_func_level")

    _delete_test_lobster_output_file()
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_FUNCTION_PROTOTYPE_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file_ref(
        "req SwRequirements.sw_req_foo1"
    ), "Requirement not found in XML files of cpp-function-prototype project."
    assert True is _is_string_in_lobster_output_file_ref(
        "req SwRequirements.sw_req_foo"
    ), "Requirement not found in XML files of cpp-function-prototype project."

    assert True is _is_string_in_lobster_output_file_just_up(
        "foo2 justification"
    ), "Justification not found in XML files of cpp-function-prototype project."
    assert True is _is_string_in_lobster_output_file_just_up(
        "foo3 justification"
    ), "Justification not found in XML files of cpp-function-prototype project."


def test_type_level(record_property) -> None:
    # lobster-trace: SwTest.tc_type_level
    """
    The test case calls the program with cpp-struct-union-class XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_numbers_struct", "req SwRequirements.sw_req_memory_union"
    and "req SwRequirements.sw_req_counter_class" strings are found in the data items.
    The test also verifies that "struct justification", "union justification" and "class justification"
    strings are found in the just_up data items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_type_level")

    _delete_test_lobster_output_file()
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_TYPE_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."
    assert True is _is_string_in_lobster_output_file_ref("req SwRequirements.sw_req_numbers_struct")
    assert True is _is_string_in_lobster_output_file_ref("req SwRequirements.sw_req_memory_union")
    assert True is _is_string_in_lobster_output_file_ref("req SwRequirements.sw_req_counter_class")

    assert True is _is_string_in_lobster_output_file_just_up("struct justification")
    assert True is _is_string_in_lobster_output_file_just_up("union justification")
    assert True is _is_string_in_lobster_output_file_just_up("class justification")


# Main *************************************************************************
