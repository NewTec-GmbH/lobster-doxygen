.. template_python documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   This file is written in ``reStructuredText`` syntax. Dor documentation see:
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

   ATTENTION!! If you want to edit "User Editable" sections, change `update_doc_from_src.py`
   otherwise they will be overwritten by intputs from the project during sphinx generation
 
.. <User editable section introduction>

TBD Project Name
================

Overview
--------

..

   TODO


Usage
-----

..

   TODO


.. code-block:: bash

   example [-h] [-v] {command} {command_options}

Detailed descriptions of arguments

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

   template_python
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
   test_empty2

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
