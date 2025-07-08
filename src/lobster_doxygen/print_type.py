"""Module for print type.

The different print message types (error, warning, info).

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************
from enum import IntEnum

# Variables ********************************************************************

# Classes **********************************************************************


class PrintType(IntEnum):
    """Different Printer Information Types."""

    ERROR = 0
    WARNING = 1
    INFO = 2


# Functions ********************************************************************
