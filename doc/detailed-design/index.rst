.. lobster_doxygen documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   This file is written in ``reStructuredText`` syntax. Dor documentation see:
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

   ATTENTION!! If you want to edit "User Editable" sections, change `update_doc_from_src.py`
   otherwise they will be overwritten by intputs from the project during sphinx generation
 
.. <User editable section introduction>
.. role:: raw-html-m2r(raw)
   :format: html


lobster-doxygen :raw-html-m2r:`<!-- omit in toc -->`
========================================================

Overview
--------

lobster-doxygen is a tool to extract requirement annotations from doxygen XML output files.
It produces the `LOBSTER common interchange format <https://github.com/bmw-software-engineering/lobster/blob/main/documentation/schemas.md>`_ as output.

One major advantage of lobster-doxygen is that the XML input files can come from many different programming languages, including C, C++, Python, Java, Objective-C, PHP, Fortran, and more. This allows  a straightforward and standardized integration into the LOBSTER TRLC toolchain.

An overview of how lobster-doxygen fits into the LOBSTER toolchain:

.. image:: doc/architecture/toolchain.png
   :target: doc/architecture/toolchain.png
   :alt: lobster-doxygen in LOBSTER toolchain


Usage
-----

lobster-doxygen is a command line application that is configured via command line arguments.

.. code-block:: md

   usage: lobster-doxygen [-h] [--version] [-o OUTPUT] [-v] doxygen_xml_folder

   Convert doxygen XML output to lobster common interchange format.

   - The source code header requires a doxygen header with at least the @file tag.
     - Rational: The doxygen XML output will consider the aliases on file level only if the file has the @file tag.
   - Tracing supports the following levels:
     - Class/Struct/Union/Namespace
     - Method
     - Function
   - Tracing on file level is possible, but not recommended and therefore the tool will abort with an error.

   To specify a requirement use @implements{REQ}.
   To specify a justification use @justification{JUSTIFICATION}.

   positional arguments:
     doxygen_xml_folder        Path to the doxygen XML output folder.

   options:
     -h, --help            show this help message and exit
     --version             show program's version number and exit
     -o OUTPUT, --output OUTPUT
                           Output file name. Default: lobster.json
     -v, --verbose         Enable verbose output.

.. </User editable section introduction>

.. <User editable section architecture>

Software Architecture
---------------------
.. toctree::
   :maxdepth: 2

   _sw-architecture/README.md
.. </User editable section architecture>

.. <User editable section source>

Software Detailed Design
------------------------
.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   lobster_item
   lobster_kind
   parse_index
   printer
   ret
   rule_check
   utils
   write_lobster_common_interchange_format_file
   __main__
.. </User editable section source> 

Testing
-------
.. <User editable section unittest>

Software Detailed Design
------------------------
.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   test_empty

.. </User editable section unittest> 

PyLint
^^^^^^
.. toctree::
   :maxdepth: 2
   
   pylint.rst

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

License information
-------------------
.. toctree::
   :maxdepth: 2

   license_include
