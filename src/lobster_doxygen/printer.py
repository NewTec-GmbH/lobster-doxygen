"""Module to print errors warning an infos.

Contains the print error function and the error messages corresponding to the
exit codes.

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
from rich import print as rprint


# Variables ********************************************************************

# Classes **********************************************************************


class Printer:
    """The printer class.
    Prints errors, warnings and infos. Infos and warnings are only printed, if
    verbose mode is set.
    """

    _print_verbose = False

    @classmethod
    def set_verbose(cls):
        # lobster-trace: SwRequirements.sw_req_cli_verbose
        """Set verbose mode for all instances of the class."""
        cls._print_verbose = True

    def print_error(self, message: str) -> None:
        """Print error message to standard error stream.

        Args:
            args (str): The error information that will be printed.
        """
        # lobster-trace: SwRequirements.sw_req_stderr_output
        rprint(f"[bold red]Error: [/bold red]{message}", end="", file=sys.stderr)

    def print_warning(self, message: str) -> None:
        """Print warning message to standard error stream.

        Args:
            args (str): The warning information that will be printed.
        """
        # lobster-trace: SwRequirements.sw_req_stderr_output
        if self._print_verbose is True:
            rprint(f"[bold yellow]Warning: [/bold yellow]{message}", end="", file=sys.stderr)

    def print_info(self, message: str) -> None:
        """Print the information to the console standard output.

        Args:
            args (str): The information that will be printed.
        """
        # lobster-trace: SwRequirements.sw_req_stdout_output
        if self._print_verbose is True:
            rprint(message)


# Functions ********************************************************************

# Main *************************************************************************
