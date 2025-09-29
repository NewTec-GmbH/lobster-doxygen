"""Test non-obligatory features of the code that do not fullfil any requirements,
but provide additional benefits.

Author: Luca Dubies (luca.dubies@newtec.de)
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
import json

from lobster_doxygen.__main__ import main
from lobster_doxygen.version import __version__

# Variables ********************************************************************

# LOBSTER output file that is created and deleted for tests.
TEST_LOBSTER_OUTPUT_FILE = "./tests/utils/output-test.json"

# Directory with Doxygen XML files.
TEST_XML_FOLDER = "./tests/utils/cpp-bad-comment/out/xml"

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


def test_tc_comment_parsing():
    # lobster-exclude: This test case is testing non required functionality.
    """
    Test if any comments parsed by doxygen in the same row as a requirement annotation are removed by the tool.
    """
    sys.argv = ["lobster-doxygen", "-v", "--output",
                TEST_LOBSTER_OUTPUT_FILE, TEST_XML_FOLDER]

    exit_code = main()

    assert exit_code == 0, "Exit Code returns no success."

    with open(TEST_LOBSTER_OUTPUT_FILE, encoding='utf-8') as interchange_file:
        interchange_output = json.load(interchange_file)

    # Comment present in xml should not be parsed as requirement id.
    assert interchange_output["data"][0]["refs"][0] == "req req1"
