# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.append(os.path.relpath("./"))
import update_doc_from_src as update_doc  # NOQA pylint: disable=C0413

# Customize to your source code location
sys.path.insert(0, os.path.abspath("../../src/lobster_doxygen"))
sys.path.insert(0, os.path.abspath("../../tests"))

# Update Overview from ./README
update_doc.update_overview()

# Copy SW Architcture to location for import in Detailed Design
update_doc.update_architecture()

# Find Python source files and add them to according autosummary section
update_doc.update_source()

# Find Unit-Test files and add them to according autosummary section
update_doc.update_unittest()

# run pyLint to include results in documentation
update_doc.update_pylint()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "lobster-doxygen"
copyright = "%Y, NewTec GmbH"
author = "Andreas Merkle"
release = "V0.???"
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # extension for python docstring
    "sphinx.ext.napoleon",  # extension to support google docstring style
    "sphinx_favicon",  # extension to support favicon for html output
    "sphinx.ext.viewcode",  # view code in documentation
    "sphinx.ext.autosummary",  # crawls python files to extract content
    "sphinxcontrib.plantuml",  # plantuml support
    "myst_parser",
]  # markdown support

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Add path to your local plantuml jar file here. Latest Version can be downloaded here:
# https://plantuml.com/de/download
plantuml = ["java", "-jar", "C:/Program Files/doxygen/bin/plantuml.jar"]

# myst settings
myst_heading_anchors = 3
myst_fence_as_directive = ["plantuml"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

autosummary_generate = True  # Automatically generate summaries
napoleon_google_docstring = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/NewTec_Logo.png"

html_theme_options = {"logo_only": False, "style_nav_header_background": "#0C2C40"}

# Add favicon
favicons = [
    {
        "rel": "icon",
        "static-file": "favicon.ico",
        "type": "image/svg+xml",
    }
]
