"""Support script for sphinx conf.py
    
    Include some additional information about the project into the documentation.
"""

# *******************************************************************************
# Copyright (c) NewTec GmbH 2024   -   www.newtec.de
# *******************************************************************************

# Imports **********************************************************************

import os
import re
import shutil
from m2r import convert

# Variables ********************************************************************

# Functions ********************************************************************


def replace_section(file_path: str, start_tag: str, end_tag: str, new_content: str):
    """
    Replace a section in a .rst file that is marked with provided start and end tags

    Args:
        file_path (str): file where to replace section
        start_tag (str): definition of section start tag
        end_tag (str): definition of section end tag
        new_content (str): new content to write between section markers
    """
    # Read the original file content
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # Define the regular expression pattern to match the section
    pattern = re.compile(
        rf"({re.escape(start_tag)})(.*?)(\s*{re.escape(end_tag)})",
        re.DOTALL  # Ensures the dot matches newlines
    )

    # Replace the matched section with the new content
    updated_content = pattern.sub(rf"\1\n{new_content}\3", content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(updated_content)
    # print(f"Updated content between {start_tag} and {end_tag}.")


def extract_md_first_heading(file_path):
    """
    Extracts the first level-one heading (# Heading) from a Markdown file.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        str: The first level-one heading, or an error message if not found.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()

        # Match the first level-one heading
        match = re.search(r"^# (.+)", content, re.MULTILINE)
        if match:
            return match.group(0)
        return "No level-one heading found in the Markdown file."

    except FileNotFoundError:
        return f"File '{file_path}' not found."


def extract_md_section(file_path, section_heading):
    """
    Extract a specific section from a Markdown file, including the section heading.

    Args:
        file_path (str): Path to the Markdown file.
        section_heading (str): The heading of the section to extract.

    Returns:
        str: The content of the section including the heading, or an error message if not found.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()

        # Use regex to match the section heading and capture its content
        pattern = rf"^(##+ {re.escape(section_heading)}\n)(.*?)(\n##+ |\Z)"
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

        if match:
            return match.group(1) + match.group(2).strip()
        return f"Section '{section_heading}' not found in the Markdown file."

    except FileNotFoundError:
        return f"File '{file_path}' not found."


def get_file_list(file_list: list, path: str = '.', file_extension: str = '') -> list:
    """ Collect file list based on extension and include file names without path and extension.

    This function crawls recursively through a folder structure and collects all
    files with the given extension.

    Args:
        path (str): Start folder
        file_extension (str): File Extension to look for
        file_list (list): Existing file list to append new entries

    Returns:
        List of tuples with found files:
        - Full file path
        - Pure file name without path and extension
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            file_list = get_file_list(file_list, file_path, file_extension)
        elif os.path.isfile(file_path) and file_path.endswith(file_extension):
            # Extract the pure file name without path and extension
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            file_list.append((file_path, file_name))
    return file_list


def update_pylint():
    """Run PyLint to generate a report that can be included by sphinx"""

    print("Update PyLint")
    pylintrc_path = os.path.abspath('../..')
    # run pylint to generate a report that can be included
    os.system(f'pylint {os.path.abspath("../../src")} --rcfile={os.path.join(pylintrc_path, ".pylintrc")} \
               --reports=y -sn --output-format=text > _pylint.tmp')

    # Fix report output, that generates an incomplete table when there are no PyLint messages
    with open('_pylint.tmp', 'r', encoding="utf-8") as file:
        content = file.read()

    # Define the pattern for the incomplete table
    table_pattern = r"\+-----------\+------------\+\n\|message id \|occurrences \|\n\+===========\+============\+"

    # Replace the pattern with a note
    updated_content = re.sub(table_pattern, "No messages", content)

    # Save the updated content to a new file (or overwrite the original file)
    with open('pylint.rst', 'w', encoding="utf-8") as file:
        file.write(updated_content)


def update_architecture():
    """Copy Architecture files from ./doc folder to detailed design for inclusion by sphinx """

    file_path = "index.rst"
    start_tag = "<User editable section architecture>"
    end_tag = ".. </User editable section architecture>"
    new_content = "\nSoftware Architecture\n---------------------\n.. toctree::\n   :maxdepth: 2\n"

    sw_arch_incl_dir = '_sw-architecture'  # sw architecture destination folder
    sw_arch_src_dir = os.path.abspath('../')  # sw architecture source folder

    if not os.path.exists(sw_arch_incl_dir):
        os.makedirs(sw_arch_incl_dir)
    files_in_doc = os.listdir(sw_arch_src_dir)
    for file_name in files_in_doc:
        if file_name.endswith('.md'):
            print(sw_arch_src_dir + file_name, sw_arch_incl_dir)
            shutil.copy(os.path.join(sw_arch_src_dir,
                        file_name), sw_arch_incl_dir)
            new_content = new_content + '\n   ' + sw_arch_incl_dir + '/' + file_name
            print(f"copy SW Architecture file to include directory:{sw_arch_src_dir}{file_name} \
                  to: {sw_arch_incl_dir}")

    # update architecture section in index.rst with copied files
    replace_section(file_path, start_tag, end_tag, new_content.rstrip())


def update_overview():
    """
    Update Overview section in index.rst with content from main README.md
    """
    print('update overview section')

    input_file = "../../README.md"
    file_path = "index.rst"
    start_tag = "<User editable section introduction>"
    end_tag = ".. </User editable section introduction>"

    heading = extract_md_first_heading(input_file)
    new_content = convert(heading)
    new_content = new_content + \
        convert(extract_md_section(input_file, 'Overview'))
    new_content = new_content + \
        convert(extract_md_section(input_file, 'Usage'))

    replace_section(file_path, start_tag, end_tag, new_content.rstrip())


def update_source():
    """Find source files and add them to index.rst"""

    print('update source section')

    file_path = "index.rst"
    start_tag = "<User editable section source>"
    end_tag = ".. </User editable section source>"
    new_content = "\nSoftware Detailed Design\n------------------------\n.. autosummary::\n"
    new_content += "   :toctree: _autosummary\n   :template: custom-module-template.rst\n   :recursive:\n\n"

    files = []
    files = get_file_list(files, '../../src', '.py')

    for _, file_name in files:
        if file_name not in ('__init__', 'version'):
            print(file_name)
            new_content += "   " + file_name + "\n"

    replace_section(file_path, start_tag, end_tag, new_content.rstrip())


def update_unittest():
    """Find unit test files and add them to index.rst"""
    print('update unittest section')

    file_path = "index.rst"
    start_tag = "<User editable section unittest>"
    end_tag = ".. </User editable section unittest>"
    new_content = "\nSoftware Detailed Design\n------------------------\n.. autosummary::\n"
    new_content += "   :toctree: _autosummary\n   :template: custom-module-template.rst\n   :recursive:\n\n"

    files = []
    files = get_file_list(files, '../../tests', '.py')

    for _, file_name in files:
        if file_name not in ('__init__', 'version'):
            print(file_name)
            new_content += "   " + file_name + "\n"

    replace_section(file_path, start_tag, end_tag, new_content.rstrip())
