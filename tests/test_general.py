"""Test the program general parts.

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
import pytest

from lobster_doxygen.__main__ import main
from lobster_doxygen.version import __version__

# Variables ********************************************************************

# LOBSTER output file that is created and deleted for tests.
TEST_LOBSTER_OUTPUT_FILE = "./tests/utils/output-test.json"

# Directory with Doxygen XML files.
TEST_XML_FOLDER = "./tests/utils/xml"

# stdout if program is called with verbose parameter
STD_OUTPUT_WITH_VERBOSE = [
    "Program arguments: ",
    f"* doxygen_xml_folder = {TEST_XML_FOLDER}",
    f"* output = {TEST_LOBSTER_OUTPUT_FILE}",
    "* verbose = True",
    "",
    "",
    "compound: main.cpp",
    "    kind: file",
    "        member: print_title",
    "            kind: function",
    "            Requirement: SwRequirements.sw_req_text_output",
    "        member: main",
    "            kind: function",
    "compound: main_group",
    "    kind: group",
    "compound: implements",
    "    kind: page (skipped)",
    "compound: src",
    "    kind: dir (skipped)",
    "",
]

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


def test_tc_cli(record_property):
    # lobster-trace: SwTests.tc_cli
    """
    Test the command-line interface (CLI) argument handling of the `main` function.
    This test simulates passing a command-line argument to the program and verifies
    that the `main` function executes successfully with the provided input.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_cli")
    print("Run test")
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    assert main() == 0


def test_tc_stdout(record_property, capsys):
    # lobster-trace: SwTests.tc_stdout
    """
    Test that the program prints its output to the standard output stream if it does not throw an
    error.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_stdout")

    sys.argv = ["lobster-doxygen", "-v", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    main()

    standard_output_captured = capsys.readouterr().out.split("\n")

    assert STD_OUTPUT_WITH_VERBOSE == standard_output_captured, "Standard output not as expected."


def test_tc_stderr(record_property, capsys):
    # lobster-trace: SwTests.tc_stderr
    """
    Test that the program prints its output to the error output stream if it is called with the
    wrong parameter.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_stderr")

    expected_error_output = [
        "usage: lobster-doxygen [-h] [--version] [-o OUTPUT] [-v] doxygen_xml_folder",
        "lobster-doxygen: error: the following arguments are required: doxygen_xml_folder",
        "",
    ]

    # Call program with no arguments
    sys.argv = ["lobster-doxygen"]

    with pytest.raises(SystemExit):
        main()

    error_output_captured = capsys.readouterr().err.split("\n")

    assert expected_error_output == error_output_captured, "Error output not as expected."


# Main *************************************************************************
