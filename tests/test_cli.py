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

import tomllib
import re
import pytest

from lobster_doxygen.__main__ import main

# Variables ********************************************************************

# Classes **********************************************************************

# Functions ********************************************************************


def test_tc_help(record_property, capsys, monkeypatch):
    # lobster-trace: SwTests.tc_help
    """
    Check for the help information in case there is no project specific converter available.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
        monkeypatch (Any): Used to mock program arguments.
    """
    record_property("lobster-trace", "SwTests.tc_help")

    # Mock program arguments to simulate running the script with --help argument.
    monkeypatch.setattr("sys.argv", ["lobster-doxygen", "--help"])

    # argparse will raise an exception if --help is provided.
    with pytest.raises(SystemExit):
        main()

    # Capture stdout and stderr.
    captured = capsys.readouterr()

    # Check just the first line of the help message.
    print(f"{captured.out}")
    regex = r"usage: lobster-doxygen \[\-h\] \[\-\-version\] \[\-o OUTPUT\] \[\-v\] doxygen_xml_folder"

    assert re.match(regex, captured.out)


def test_tc_version(record_property, capsys, monkeypatch):
    # lobster-trace: SwTests.tc_version
    """
    Check that with '--version' argument program output is the tool name with version from pyproject.toml.

    Args:
        record_property (Any): Used to inject the test case reference into the test results.
        capsys (Any): Used to capture stdout and stderr.
        monkeypatch (Any): Used to mock program arguments.
    """
    record_property("lobster-trace", "SwTests.tc_version")

    # Mock program arguments to simulate running the script --version argument.
    monkeypatch.setattr("sys.argv", ["lobster-doxygen", "--version"])

    # argparse will raise an exception if --version is provided.
    with pytest.raises(SystemExit):
        main()

    # Capture stdout and stderr.
    captured = capsys.readouterr()

    # Check just the first line of the version message.
    print(f"{captured.out}")

    # Get version from pyproject.toml.
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    current_version = data["project"]["version"]

    expected_program_output = f"lobster-doxygen {current_version}"

    # Check that program output is as expected.
    assert re.match(expected_program_output, captured.out)


# Main *************************************************************************
