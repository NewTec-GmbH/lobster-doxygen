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
import pytest

from lobster_doxygen.__main__ import main

# Variables ********************************************************************

# LOBSTER output file that is created and deleted for tests.
TEST_LOBSTER_OUTPUT_FILE = "./tests/utils/output-test.json"

# Directory with Doxygen XML files.
TEST_XML_FOLDER = "./tests/utils/xml"

# Directory with Doxygen XML files from cpp-level-test project, to test @implementation and @justification.
TEST_LEVEL_XML_FOLDER = "./tests/utils/cpp-level-test/out/xml"

# Directory with Doxygen XML files from cpp-file-requirement project, to test requirement abort rule on file level.
TEST_RULE_FILE_REQUIREMENT_XML_FOLDER = "./tests/utils/cpp-rule-tests/cpp-file-requirement/out/xml"

# Directory with Doxygen XML files from cpp-file-justification project, to test justification abort rule on file level.
TEST_RULE_FILE_JUSTIFICATION_XML_FOLDER = "./tests/utils/cpp-rule-tests/cpp-file-justification/out/xml"

# Directory with Doxygen XML files from cpp-class-and-method-requirement project, to test
# requirements abort rule on class and method level.
TEST_RULE_CLASS_AND_METHOD_REQUIREMENTS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-class-and-method-requirement/out/xml"
)

# Directory with Doxygen XML files from cpp-class-and-method-justification project, to test
# justifications abort rule on class and method level.
TEST_RULE_CLASS_AND_METHOD_JUSTIFICATIONS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-class-and-method-justification/out/xml"
)


# Directory with Doxygen XML files from cpp-class-and-interface-requirement project, to test
# requirements abort rule on class and interface level.
TEST_RULE_CLASS_AND_INTERFACE_REQUIREMENTS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-class-and-interface-requirement/out/xml"
)

# Directory with Doxygen XML files from cpp-class-and-interface-justification project, to test
# justifications abort rule on class and interface level.
TEST_RULE_CLASS_AND_INTERFACE_JUSTIFICATIONS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-class-and-interface-justification/out/xml"
)


# Directory with Doxygen XML files from cpp-namespace-and-function-requirement project, to test
# requirements abort rule on namespace and function level.
TEST_RULE_NAMESPACE_AND_FUNCTION_REQUIREMENTS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-namespace-and-function-requirement/out/xml"
)

# Directory with Doxygen XML files from cpp-namespace-and-function-justification project, to test
# justifications abort rule on namespace and function level.
TEST_RULE_NAMESPACE_AND_FUNCTION_JUSTIFICATIONS_XML_FOLDER = (
    "./tests/utils/cpp-rule-tests/cpp-namespace-and-function-justification/out/xml"
)

# Directory with Doxygen XML files from cpp-unspecified project, to test supported kind with no
# requirement or justification.
TEST_UNSPECIFIED_XML_FOLDER = "./tests/utils/cpp-unspecified/out/xml"

# Empty directory with no XML files.
EMPTY_FOLDER = "./tests/utils/empty_folder"

# Directory with Doxygen XML files from cpp-no-trace project, to test that providing no
# source code and the generated doxygen XML code does not cause an error.
TEST_NO_TRACE_XML_FOLDER = "./tests/utils/cpp-no-trace/out/xml"

# Expected data in LOBSTER file for TEST_XML_FOLDER.
EXPECTED_LOBSTER_INTERCHANGE_FILE_CONTENT = [
    "{",
    '    "data": [',
    "        {",
    '            "tag": "cpp main_8cpp_1ab7c242550b0e07889a040b75b58956ff",',
    '            "location": {',
    '                "kind": "file",',
    '                "file": "src/main.cpp",',
    '                "line": 31,',
    '                "column": 13',
    "            },",
    '            "name": "print_title",',
    '            "messages": [],',
    '            "just_up": [],',
    '            "just_down": [],',
    '            "just_global": [],',
    '            "refs": [',
    '                "req SwRequirements.sw_req_text_output"',
    "            ],",
    '            "language": "C++",',
    '            "kind": "Function"',
    "        },",
    "        {",
    '            "tag": "cpp main_8cpp_1a840291bc02cba5474a4cb46a9b9566fe",',
    '            "location": {',
    '                "kind": "file",',
    '                "file": "src/main.cpp",',
    '                "line": 38,',
    '                "column": 5',
    "            },",
    '            "name": "main",',
    '            "messages": [],',
    '            "just_up": [],',
    '            "just_down": [],',
    '            "just_global": [],',
    '            "refs": [],',
    '            "language": "C++",',
    '            "kind": "Function"',
    "        },",
    "        {",
    '            "tag": "unknown  group__main__group",',
    '            "location": {',
    '                "kind": "file",',
    '                "file": "",',
    '                "line": 0,',
    '                "column": 0',
    "            },",
    '            "name": "main_group",',
    '            "messages": [],',
    '            "just_up": [],',
    '            "just_down": [],',
    '            "just_global": [],',
    '            "refs": [],',
    '            "language": "None",',
    '            "kind": "Group"',
    "        }",
    "    ],",
    '    "generator": "lobster-doxygen",',
    '    "schema": "lobster-imp-trace",',
    '    "version": 3',
    "}",
]

WARNING_OUTPUT_NO_LOBSTER_ITMES = "Warning: No lobster items found in the doxygen XML output."

# Classes **********************************************************************

# Functions ********************************************************************


@pytest.fixture(autouse=True)
def _setup_and_teardown():
    # lobster-exclude: This is a simple helper function that prepares and cleanup the tests.
    """Before running the test, delete the LOBSTER file if it exists."""
    # Preparation:
    if Path(TEST_LOBSTER_OUTPUT_FILE).exists() and Path(TEST_LOBSTER_OUTPUT_FILE).is_file():
        Path(TEST_LOBSTER_OUTPUT_FILE).unlink()
    yield
    # Teardown:


def _get_data_items_from_lobster_file() -> dict:
    # lobster-exclude: Helper function for all tests in module.
    """
    Get dictionary of data section in TEST_LOBSTER_OUTPUT file.

    Returns:
        dict: Dictionary of data section.
    """
    with open(TEST_LOBSTER_OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data_items = data.get("data", [])
    return data_items


def _is_string_in_lobster_output_file(search_string: str, property_to_lock: str) -> bool:
    # lobster-exclude: Helper function for all tests in module.
    """
    Checks if search_string is TEST_LOBSTER_OUTPUT_FILE file in a property of data section.

    Args:
        search_string (str): Search string to lock for.
        property_to_lock (str): Specific data item property to look for string.

    Returns:
        bool: True is search_string is found.
    """
    data_items = _get_data_items_from_lobster_file()
    for data_item in data_items:
        if search_string in data_item[property_to_lock]:
            return True

    return False


def test_tc_output_file_format_verify_generated_file(record_property) -> None:
    # lobster-trace: SwTests.tc_output_file_format
    """
    Test calls program with doxygen_xml_folder path where a valid index.xml file is inside and
    checks that the program runs successfully.
    The test verifies that the generated LOBSTER common interchange file contains the expected data.
    """
    record_property("lobster-trace", "SwTests.tc_output_file_format")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    exit_code = main()
    with open(TEST_LOBSTER_OUTPUT_FILE, "r", encoding="utf-8") as lobster_file:
        lobster_file_content = [line.strip("\n")
                                for line in lobster_file.readlines()]

    assert exit_code == 0, "Exit Code returns no success."
    assert lobster_file_content == EXPECTED_LOBSTER_INTERCHANGE_FILE_CONTENT


def test_tc_output_file_format_program_with_directory_with_no_index_file(record_property, capsys) -> None:
    # lobster-trace: SwTests.tc_output_file_format
    """
    After that program is called with doxygen_xml_folder path where no index.xml file is inside
    and checks that the program returns an error.

    Args:
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_output_file_format")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, EMPTY_FOLDER]

    exit_code = main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")
    assert exit_code != 0, "Exit Code returns success."
    assert error_output == [
        "Error: No doxygen index.xml file in doxygen_xml_folder ", f"{EMPTY_FOLDER}."]


def test_tc_function_level(record_property) -> None:
    # lobster-trace: SwTests.tc_function_level
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_prototype" and "req SwRequirements.sw_req_function" strings
    are found in the data items.
    The test also verifies that "Prototype justification" and "Function justification" strings are found in
    the just_up data items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_function_level")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_prototype", "refs"
    ), "Requirement not found in XML files of cpp-function-prototype project."
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_function", "refs"
    ), "Requirement not found in XML files of cpp-function-prototype project."

    assert True is _is_string_in_lobster_output_file(
        "Prototype justification", "just_up"
    ), "Justification not found in XML files of cpp-function-prototype project."
    assert True is _is_string_in_lobster_output_file(
        "Function justification", "just_up"
    ), "Justification not found in XML files of cpp-function-prototype project."


def test_tc_type_level(record_property) -> None:
    # lobster-trace: SwTests.tc_type_level
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_struct", "req SwRequirements.sw_req_union"
    and "req SwRequirements.sw_req_class" strings are found in the data items.
    The test also verifies that "Struct justification", "Union justification" and "Class justification"
    strings are found in the just_up data items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_type_level")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_struct", "refs")
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_union", "refs")
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_class", "refs")

    assert True is _is_string_in_lobster_output_file(
        "Struct justification", "just_up")
    assert True is _is_string_in_lobster_output_file(
        "Union justification", "just_up")
    assert True is _is_string_in_lobster_output_file(
        "Class justification", "just_up")


def test_tc_namespace_level(record_property) -> None:
    # lobster-trace: SwTests.tc_namespace_level
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_namespace" string are found in the data items.
    The test also verifies that "namespace justification" string are found in the just_up data
    items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_namespace_level")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_namespace", "refs")
    assert True is _is_string_in_lobster_output_file(
        "Namespace justification", "just_up")


def test_tc_method_level(record_property) -> None:
    # lobster-trace: SwTests.tc_method_level
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_public_method",
    "req SwRequirement.sw_req_protected_method" and "req SwRequirement.sw_req_private_method"
    strings are found in refs of the data items.
    The test also verifies that "Public method justification", "Protected method justification"
    and "Private method justification" strings are found in the just_up data
    items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_method_level")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_public_method", "refs")
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_protected_method", "refs")
    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_private_method", "refs")

    assert True is _is_string_in_lobster_output_file(
        "Public method justification", "just_up")
    assert True is _is_string_in_lobster_output_file(
        "Protected method justification", "just_up")
    assert True is _is_string_in_lobster_output_file(
        "Private method justification", "just_up")


def test_tc_interface_level(record_property) -> None:
    # lobster-trace: SwTests.tc_interface_level
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_interface_method" string is found in refs of the
    data items.
    The test also verifies that "Interface method justification" string is found in the just_up data
    items.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """

    record_property("lobster-trace", "SwTests.tc_interface_level")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_interface_method", "refs")
    assert True is _is_string_in_lobster_output_file(
        "Interface method justification", "just_up")


def test_tc_no_group(record_property) -> None:
    # lobster-trace: SwTests.tc_no_group
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_no_group_function" string is found in refs of the
    data items.
    The test also verifies that "No group struct justification" string is found in the just_up data
    items.
    The function and struct are in no group because there is no defgroup or ingroup in the file
    header.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """

    record_property("lobster-trace", "SwTests.tc_no_group")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_no_group_function", "refs")
    assert True is _is_string_in_lobster_output_file(
        "No group struct justification", "just_up")


def test_tc_group(record_property) -> None:
    # lobster-trace: SwTests.tc_group
    """
    The test case calls the program with cpp-level-test XML folder as doxygen_xml_folder and
    verifies that the "req SwRequirement.sw_req_in_group_function" string is found in refs of the
    data items.
    The test also verifies that "In group struct justification" string is found in the just_up data
    items.
    The function and struct are in a group because defgroup or ingroup is defined in the file
    header.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """

    record_property("lobster-trace", "SwTests.tc_group")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_LEVEL_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    assert True is _is_string_in_lobster_output_file(
        "req SwRequirements.sw_req_in_group_function", "refs")
    assert True is _is_string_in_lobster_output_file(
        "In group struct justification", "just_up")


def test_tc_rule_file_abort_with_requirement_on_file_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_file
    """
    The test case calls the program with cpp-file-requirement XML folder as doxygen_xml_folder and
    ensures that the program aborts with a no success exit code.
    In the cpp-file-requirement project a requirement is specified at file level.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_file")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_RULE_FILE_REQUIREMENT_XML_FOLDER]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_file_abort_with_justification_on_file_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_file
    """
    The test case calls the program with cpp-file-justification XML folder as doxygen_xml_folder and
    ensures that the program aborts with a no success exit code.
    In the cpp-file-justification project a justification is specified at file level.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_file")

    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_RULE_FILE_JUSTIFICATION_XML_FOLDER]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_requirements_in_class_and_method_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-class-and-method-requirement XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-class-and-method-requirement project, requirements are specified at class and
    method level of the class.
    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_CLASS_AND_METHOD_REQUIREMENTS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_justification_in_class_and_method_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-class-and-method-justification XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-class-and-method-justification project, justifications are specified at class and
    method level of the class.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_CLASS_AND_METHOD_JUSTIFICATIONS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_requirements_in_class_and_interface_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-class-and-interface-requirement XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-class-and-interface-requirement project, requirements are specified at class and
    interface method level of the class.
    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """

    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_CLASS_AND_INTERFACE_REQUIREMENTS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_justification_in_class_and_interface_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-class-and-interface-justification XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-class-and-interface-justification project, justifications are specified at class and
    interface method level of the class.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_CLASS_AND_INTERFACE_JUSTIFICATIONS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_requirements_in_namespace_and_function_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-namespace-and-function-requirement XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-namespace-and-function-requirement project, requirements are specified at namespace and
    function level of the namespace.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_NAMESPACE_AND_FUNCTION_REQUIREMENTS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_rule_class_abort_with_justification_in_namespace_and_function_level(record_property) -> None:
    # lobster-trace: SwTests.tc_rule_class
    """
    The test case calls the program with cpp-namespace-and-function-justification XML folder as
    doxygen_xml_folder and ensures that the program aborts with a no success exit code.
    In the cpp-namespace-and-function-justification project, justifications are specified at namespace and
    function level of the namespace.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_rule_class")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_RULE_NAMESPACE_AND_FUNCTION_JUSTIFICATIONS_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code != 0, "Exit Code returns success."


def test_tc_unspecified(record_property) -> None:
    # lobster-trace: SwTests.tc_unspecified
    """
    This test case calls the program with cpp-unspecified XML folder as doxygen_xml_folder and
    ensures that the program is executed without errors.
    In the cpp-unspecified project are all supported levels without a requirements or justifications.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_unspecified")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_UNSPECIFIED_XML_FOLDER,
    ]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."


def test_tc_no_trace(record_property, capsys) -> None:
    # lobster-trace: SwTests.tc_no_trace
    """
    This test case calls the program with cpp-no-trace XML folder as doxygen_xml_folder and
    ensures that the program is executed without errors.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture the output of the program.
    """
    record_property("lobster-trace", "SwTests.tc_no_trace")

    sys.argv = [
        "lobster-doxygen",
        "-v",
        "--output",
        TEST_LOBSTER_OUTPUT_FILE,
        TEST_NO_TRACE_XML_FOLDER,
    ]

    exit_code = main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")

    assert [
        WARNING_OUTPUT_NO_LOBSTER_ITMES] == error_output, f"Program exit with error: {error_output}"

    assert exit_code == 0, "Exit Code returns no success."

# Main *************************************************************************
