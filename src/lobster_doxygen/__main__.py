"""lobster-doxygen main module.

Script to generate the lobster common interchange format from a doxygen XML output.

Author: Andreas Merkle (andreas.merkle@newtec.de)
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

import argparse
import sys

try:
    from lobster_doxygen.version import __version__, __author__, __email__, __repository__, __license__
except ModuleNotFoundError:
    # provide dummy information when not installed as package but called directly
    # also necessary to get sphinx running without error
    __version__ = "dev"
    __author__ = "Andreas Merkle"
    __email__ = "andreas.merkle@newtec.de"
    __repository__ = "https://github.com/NewTec-GmbH/lobster-doxygen.git"
    __license__ = "GPLv3"
from lobster_doxygen.ret import Ret
from lobster_doxygen.printer import Printer
from lobster_doxygen.rule_check import rule_check
from lobster_doxygen.write_lobster_config import write_lobster_config
from lobster_doxygen.parse_index import parse_index

# Variables ********************************************************************

PROG_NAME = "lobster-doxygen"
PROG_DESC = "Script to generate the lobster common interchange format from a doxygen XML output."
PROG_COPYRIGHT = "Copyright (c) 2025 NewTec GmbH"

LOG = Printer()

# Functions ********************************************************************


def add_parser() -> argparse.ArgumentParser:
    """Add parser for command line arguments and
        set the execute function of each
        cmd module as callback for the subparser command.
        Return the parser after all the modules have been registered
        and added their subparsers.


    Returns:
        obj:  The parser object for command line arguments.
    """
    # Create argument parser which accepts one mandatory parameter for the doxygen
    # folder that contains the XML output.
    parser = argparse.ArgumentParser(prog=PROG_NAME, description=PROG_DESC, epilog=PROG_COPYRIGHT)

    parser.add_argument("--version", action="version", version="%(prog)s " + __version__)
    parser.add_argument("doxygen_folder", type=str, help="Path to the doxygen XML output folder.")
    parser.add_argument("-o", "--output", type=str, help="Output file name.", default="lobster.cfg")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")

    return parser


def main() -> Ret.CODE:
    """Main function to convert doxygen XML output to lobster common interchange format.

    Returns:
        int: System exit status
    """
    ret_status = Ret.CODE.RET_OK
    printer = Printer()
    args = None

    # Get parser
    parser = add_parser()

    # Parse command line arguments.
    # If error occurs, exits the program from this point with code 2.
    args = parser.parse_args()

    if args is None:
        ret_status = Ret.CODE.RET_ERROR_ARGPARSE
    else:
        # In verbose mode print all program arguments
        if args.verbose:
            printer.set_verbose()
            print("Program arguments: ")

            for arg in vars(args):
                print(f"* {arg} = {vars(args)[arg]}")
            print("\n")

        # Check if the doxygen folder exists.
        if args.doxygen_folder:

            lobster_items = parse_index(args.doxygen_folder)

            if rule_check(lobster_items) is True:
                write_lobster_config(args.output, lobster_items)
                ret_status = Ret.CODE.RET_OK

    if ret_status is not Ret.CODE.RET_OK:
        print(Ret.MSG[ret_status])

    return ret_status


# Main *************************************************************************


if __name__ == "__main__":
    sys.exit(main())
