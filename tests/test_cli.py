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

    # Mock program arguments to simulate running the script without any arguments.
    monkeypatch.setattr("sys.argv", ["lobster-doxygen", "--help"])

    # argparse will raise an exception if --help is provided.
    with pytest.raises(SystemExit):
        main()

    # Capture stdout and stderr.
    captured = capsys.readouterr()

    # Check just the first line of the help message.
    print(f"{captured.out}")
    regex = r"usage: lobster-doxygen \[\-h\] \[\-\-version\] \[\-o OUTPUT\] \[\-v\] doxygen_xml_folder"

    print(f"{regex=}")
    assert re.match(regex, captured.out)


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
