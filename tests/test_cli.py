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

# Classes **********************************************************************

# Functions ********************************************************************


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

    expected_output_file = "./tests/utils/output-test.json"

    # Delete the LOBSTER file if it exists
    if Path(expected_output_file).exists() and Path(expected_output_file).is_file():
        Path(expected_output_file).unlink()

    sys.argv = ["lobster-doxygen", "--output", expected_output_file, "./tests/utils/xml"]

    main()

    captured = capsys.readouterr()
    error_output = captured.err.split("\n")

    assert error_output == [""], f"Program exit with error: {error_output}"
    assert Path(expected_output_file).exists(), "Expected output file was not created"
    assert Path(expected_output_file).is_file(), "Expected output path is not a file"


# Main *************************************************************************
