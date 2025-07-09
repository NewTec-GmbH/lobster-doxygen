"""Module to print errors warning an infos.

Contains the print error function and the error messages corresponding to the
exit codes.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# lobster-doxygen
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Imports **********************************************************************
from colorama import Fore, Style

from lobster_doxygen.print_type import PrintType

# Variables ********************************************************************

COLOR = {PrintType.ERROR: Fore.RED, PrintType.WARNING: Fore.YELLOW, PrintType.INFO: Fore.WHITE}

TYPE = {PrintType.ERROR: "Error", PrintType.WARNING: "Warning", PrintType.INFO: "Info"}

INFO_TAB = "      "


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

    def print_error(self, err_type: PrintType, *args: str) -> None:
        """Print the exit error.

        Args:
            type (PrintType)    The type of the msg (Error, Warning or Info).
            args (*str):        The error information that will be printed.
        """

        if err_type is PrintType.WARNING and self._print_verbose:
            print(COLOR[err_type] + TYPE[err_type] + ": " + Style.RESET_ALL, end="")

        elif err_type is PrintType.ERROR:
            print(COLOR[err_type] + TYPE[err_type] + ": " + Style.RESET_ALL, end="")

        first_line = True
        for arg in args:
            if first_line:
                print(arg)
                first_line = False
            else:
                print(INFO_TAB + arg)

    def print_info(self, *args: str) -> None:
        """Print the information to the console.

        Args:
            args (*str):          The information that will be printed.
        """
        first_line = True

        if self._print_verbose:
            for arg in args:
                if first_line:
                    print("Info: " + arg)
                    first_line = False
                else:
                    print(INFO_TAB + arg)


# Functions ********************************************************************
