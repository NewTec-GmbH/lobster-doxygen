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
import pytest

from lobster_doxygen.__main__ import main
from lobster_doxygen.version import __version__

# Variables ********************************************************************

# Classes **********************************************************************

# Functions ********************************************************************


def test_tc_help(record_property, capsys):
    # lobster-trace: SwTests.tc_help
    """
    Test the command-line interface (CLI) help message of the `main` function.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
    """
    record_property("lobster-trace", "SwTests.tc_help")

    expected_help_output_lines = [
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

    assert expected_help_output_lines == captured.out.split("\n")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


def test_tc_version(record_property, capsys):
    # lobster-trace: SwTests.tc_version
    """
    Test the command-line interface (CLI) version message of the `main` function.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
        monkeypatch (Any): Used to mock program arguments.
    """
    record_property("lobster-trace", "SwTests.tc_version")

    expected_help_output_lines = [
        f"lobster-doxygen {__version__}",
        "",
    ]

    sys.argv = ["lobster-doxygen", "--version"]

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()

    captured = capsys.readouterr()

    assert expected_help_output_lines == captured.out.split("\n")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


# Main *************************************************************************
