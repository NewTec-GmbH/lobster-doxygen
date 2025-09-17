"""lobster-doxygen main module.

Tool to generate LOBSTER common interchange format file from a doxygen XML output.

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
from lobster_doxygen.doxygen_to_lobster_converter import convert_doxygen_xml_to_lobster_common_interchange_format

# Variables ********************************************************************

PROG_NAME = "lobster-doxygen"

# Requirement alias, which is configured in the doxygen configuration, see alias.
_REQ_ALIAS = "implements"

# Justification alias, which is configured in the doxygen configuration, see alias.
_JUSTIFICATION_ALIAS = "justification"

# Command line help description.
_HELP_DESCRIPTION = (
    "Convert doxygen XML output to lobster common interchange format.\n"
    "\n"
    "- The source code header requires a doxygen header with at least the @file tag.\n"
    "  - Rational: The doxygen XML output will consider the aliases on file level only if the file has the @file tag.\n"
    "- Tracing supports the following levels:\n"
    "  - Class/Struct/Union/Namespace\n"
    "  - Method\n"
    "  - Function\n"
    "- Tracing on file level is possible, but not recommended and therefore the tool will abort with an error.\n"
    "\n"
    f"To specify a requirement use @{_REQ_ALIAS}"
    "{REQ}.\n"
    f"To specify a justification use @{_JUSTIFICATION_ALIAS}"
    "{JUSTIFICATION}.\n"
)

LOG = Printer()


# Classes **********************************************************************


class RawDescriptionHelpFormatterWithNL(argparse.RawDescriptionHelpFormatter):
    # lobster-trace: SwRequirements.sw_req_cli_help
    """Custom help formatter to keep newlines in the description."""

    def _fill_text(self, text, width, indent):
        """Fill the text with the given width and indent.

        Args:
            text (str): The text to format.
            width (int): The width of the output text.
            indent (str): The indentation to apply.

        Returns:
            str: The formatted text.
        """
        # Keep newlines as is
        return "".join([indent + line + "\n" for line in text.splitlines()])


# Functions ********************************************************************


def _add_parser() -> argparse.ArgumentParser:
    """Add parser for command line arguments and set the execute function of
    each cmd module as callback for the subparser command.
    Return the parser after all the modules have been registered and added their
    subparsers.

    Returns:
        obj:  The parser object for command line arguments.
    """
    # Create argument parser which accepts one mandatory parameter for the doxygen
    # folder that contains the XML output.

    # lobster-trace: SwRequirements.sw_req_cli_help
    # lobster-trace: SwRequirements.sw_req_cli_version
    # lobster-trace: SwRequirements.sw_req_cli_doxygen_xml_folder
    # lobster-trace: SwRequirements.sw_req_cli_output
    # lobster-trace: SwRequirements.sw_req_cli_verbose
    parser = argparse.ArgumentParser(
        description=_HELP_DESCRIPTION, formatter_class=RawDescriptionHelpFormatterWithNL)
    parser.add_argument("--version", action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("doxygen_xml_folder", type=str,
                        help="Path to the doxygen XML output folder.")
    parser.add_argument(
        "-o", "--output", type=str, help="Output file name. Default: lobster.json", default="lobster.json"
    )
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose output.")

    return parser


def _print_program_arguments(args: argparse.Namespace) -> None:
    # lobster-trace: SwRequirements.sw_req_cli_verbose
    """Print program argument information.

    Args:
        args (argparse.Namespace): Program arguments from user.
    """
    LOG.print_info("Program arguments: ")
    for arg in vars(args):
        LOG.print_info(f"* {arg} = {vars(args)[arg]}")
    LOG.print_info("\n")

def main() -> Ret:
    """Main function to convert doxygen XML output to lobster common interchange format.

    Returns:
        int: System exit status
    """
    # lobster-trace: SwRequirements.sw_req_cli
    # lobster-trace: SwRequirements.sw_req_stdout_output
    ret_status = Ret.RET_OK
    args = None

    # Get parser
    parser = _add_parser()

    # Parse command line arguments.
    # If error occurs, exits the program from this point with code 2.
    args = parser.parse_args()

    if args is None:
        ret_status = Ret.RET_ERROR_ARGPARSE
    else:
        # In verbose mode print all program arguments
        if args.verbose:
            LOG.set_verbose()
            _print_program_arguments(args)

        # Check if the doxygen folder exists in the arguments.
        if args.doxygen_xml_folder:
            ret_status = convert_doxygen_xml_to_lobster_common_interchange_format(
                args.doxygen_xml_folder, args.output)

    return ret_status


# Main *************************************************************************


if __name__ == "__main__":
    sys.exit(main())
