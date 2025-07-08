"""Module to represent the kind of lobster item.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

import enum

# Variables ********************************************************************

# Classes **********************************************************************


class LobsterKind(enum.Enum):
    """Enum to represent the kind of lobster item."""

    UNDEFINED = "Undefined"
    FUNCTION = "Function"
    PROTOTYPE = "Prototype"
    METHOD = "Method"
    CLASS = "Class"
    STRUCT = "Struct"
    INTERFACE = "Interface"
    FILE = "File"
    NAMESPACE = "Namespace"


# Functions ********************************************************************
