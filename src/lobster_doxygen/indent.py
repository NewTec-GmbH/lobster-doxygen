"""Module set indent to string.

Author: Andreas Merkle (andreas.merkle@newtec.de)
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

# Variables ********************************************************************

_INDENT_SPACES = 4

# Classes **********************************************************************

# Functions ********************************************************************


def indent(level: int, text: str) -> str:
    """Indent the given text with the specified level.

    Args:
        level (int): The indentation level.
        text (str): The text to be indented.

    Returns:
        str: The indented text.
    """
    return " " * (_INDENT_SPACES * level) + text
