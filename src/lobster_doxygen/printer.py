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

from colorama import Fore, Style

from lobster_doxygen.utils import indent

# Variables ********************************************************************

# Classes **********************************************************************


class Printer:
    """The printer class.
    Prints errors, warnings and infos. Infos and warnings are only printed, if
    verbose mode is set.
    """

    _print_verbose = False

    def __init__(self):
        pass

    @classmethod
    def set_verbose(cls):
        """Set verbose mode for all instances of the class."""
        cls._print_verbose = True

    def print_error(self, *args: str) -> None:
        """Print error message.

        Args:
            args (*str): The error information that will be printed.
        """

        print(Fore.RED + "Error: " + Style.RESET_ALL, end="")
        Printer._print_args(*args)

    def print_warning(self, *args: str) -> None:
        """Print warning message.

        Args:
            args (*str): The warning information that will be printed.
        """

        print(Fore.YELLOW + "Warning: " + Style.RESET_ALL, end="")
        Printer._print_args(*args)

    def print_info(self, *args: str) -> None:
        """Print the information to the console.

        Args:
            args (*str): The information that will be printed.
        """
        Printer._print_args(*args)

    @classmethod
    def _print_args(cls, *args: str) -> None:
        """Prints args.

        Args:
            args (*str): String to print.
        """
        first_line = True
        for arg in args:
            if first_line:
                print(arg)
                first_line = False
            else:
                print(indent(1, arg))


# Functions ********************************************************************

# Main *************************************************************************
