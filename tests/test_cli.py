"""Test the program command line interface.

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

# Directory with Doxygen XML files.
EMPTY_FOLDER = "./tests/utils/empty_folder"

# Classes **********************************************************************

# Functions ********************************************************************


def _delete_test_lobster_output_file() -> None:
    """Delete the LOBSTER file if it exists."""
    if Path(TEST_LOBSTER_OUTPUT_FILE).exists() and Path(TEST_LOBSTER_OUTPUT_FILE).is_file():
        Path(TEST_LOBSTER_OUTPUT_FILE).unlink()


def test_tc_cli(record_property):
    # lobster-trace: SwTests.tc_cli
    """
    Test the command-line interface (CLI) argument handling of the `main` function.
    This test simulates passing a command-line argument to the program and verifies
    that the `main` function executes successfully with the provided input.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_cli")

    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    _delete_test_lobster_output_file()

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
    _delete_test_lobster_output_file()

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


def test_tc_help(record_property, capsys) -> None:
    # lobster-trace: SwTests.tc_help
    """
    Test the command-line interface (CLI) help message of the `main` function.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_help")

    expected_output_lines = [
        "usage: lobster-doxygen [-h] [--version] [-o OUTPUT] [-v] doxygen_xml_folder",
        "",
        "Convert doxygen XML output to lobster common interchange format.",
        "",
        "- The source code header requires a doxygen header with at least the @file tag.",
        "  - Rational: The doxygen XML output will consider the aliases on file level only if the file has the @file tag.",
        "- Tracing supports the following levels:",
        "  - Class/Struct/Union/Namespace",
        "  - Method",
        "  - Function",
        "- Tracing on file level is possible, but not recommended and therefore the tool will abort with an error.",
        "",
        "To specify a requirement use @implements{REQ}.",
        "To specify a justification use @justification{JUSTIFICATION}.",
        "",
        "positional arguments:",
        "  doxygen_xml_folder    Path to the doxygen XML output folder.",
        "",
        "options:",
        "  -h, --help            show this help message and exit",
        "  --version             show program's version number and exit",
        "  -o OUTPUT, --output OUTPUT",
        "                        Output file name. Default: lobster.json",
        "  -v, --verbose         Enable verbose output.",
        "",
    ]

    sys.argv = ["lobster-doxygen", "--help"]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    captured = capsys.readouterr()

    assert expected_output_lines == captured.out.split("\n"), "Program standard output not as expected."
    assert pytest_wrapped_e.type == SystemExit, "Program exit not as expected."
    assert pytest_wrapped_e.value.code == 0, "ExitCode not as expected."


def test_tc_version(record_property, capsys) -> None:
    # lobster-trace: SwTests.tc_version
    """
    Test the command-line interface (CLI) version message of the `main` function.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_version")

    expected_output_lines = [
        f"lobster-doxygen {__version__}",
        "",
    ]

    sys.argv = ["lobster-doxygen", "--version"]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    captured = capsys.readouterr()

    assert expected_output_lines == captured.out.split("\n"), "Program standard output not as expected."
    assert pytest_wrapped_e.type == SystemExit, "Program exit not as expected."
    assert pytest_wrapped_e.value.code == 0, "ExitCode not as expected."


def test_tc_output(record_property, capsys) -> None:
    # lobster-trace: SwTest.tc_output
    """
    Test to confirm that the program creates the expected output file when a '--output' argument
    is provided, and that it exits without error messages.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_output")

    _delete_test_lobster_output_file()

    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")

    assert error_output == [""], f"Program exit with error: {error_output}"
    assert Path(TEST_LOBSTER_OUTPUT_FILE).exists(), "Expected output file was not created"
    assert Path(TEST_LOBSTER_OUTPUT_FILE).is_file(), "Expected output path is not a file"


def test_tc_verbose(record_property, capsys) -> None:
    # lobster-trace: SwTest.tc_verbose
    """
    This test verifies the verbose output of the lobster-doxygen program when run with the -v (verbose) flag.
    It ensures that the program produces the expected stdout output when parsing the specified Doxygen XML
    directory.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_verbose")

    sys.argv = ["lobster-doxygen", "-v", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")
    standard_output = captured.out.split("\n")

    _delete_test_lobster_output_file()

    assert error_output == [""], f"Program exit with error: {error_output}"
    assert STD_OUTPUT_WITH_VERBOSE == standard_output, "Standard output not as expected."


def test_tc_doxygen_xml_folder(record_property) -> None:
    # lobster-trace: SwTest.tc_doxygen_xml_folder
    """
    Test calls program with and without positional doxygen_xml_folder argument and verifies
    that the exit code is as expected.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
    """
    record_property("lobster-trace", "SwTests.tc_doxygen_xml_folder")

    _test_program_with_positional_doxygen_xml_folder_argument()
    _test_program_without_positional_doxygen_xml_folder_argument()


def _test_program_with_positional_doxygen_xml_folder_argument() -> None:
    """
    Test calls program with positional doxygen_xml_folder path and checks that program returns
    success exit code.
    """
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."


def _test_program_without_positional_doxygen_xml_folder_argument() -> None:
    """
    Test calls program without positional doxygen_xml_folder path and checks that program returns
    no success exit code.
    """
    sys.argv = ["lobster-doxygen", "--output", TEST_LOBSTER_OUTPUT_FILE]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    assert pytest_wrapped_e.value.code != 0, "Exit Code returns success."


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


# Main *************************************************************************
