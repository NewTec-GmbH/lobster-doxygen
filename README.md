# lobster-doxygen <!-- omit in toc -->

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://choosealicense.com/licenses/gpl-3.0/) [![Repo Status](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip) [![CI](https://github.com/NewTec-GmbH/lobster-doxygen/actions/workflows/test.yml/badge.svg)](https://github.com/NewTec-GmbH/lobster-doxygen/actions/workflows/test.yml)

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Doxygen XML files](#doxygen-xml-files)
- [Examples](#examples)
- [SW Documentation](#sw-documentation)
- [Used Libraries](#used-libraries)
- [Issues, Ideas And Bugs](#issues-ideas-and-bugs)
- [License](#license)
- [Contribution](#contribution)

## Overview

lobster-doxygen is a tool to extract requirement annotations from doxygen XML output files.
It produces the [LOBSTER common interchange format](https://github.com/bmw-software-engineering/lobster/blob/main/documentation/schemas.md) as output.

One major advantage of lobster-doxygen is that the XML input files can come from many different programming languages, including C, C++, Python, Java, Objective-C, PHP, Fortran, and more. This allows  a straightforward and standardized integration into the LOBSTER TRLC toolchain.

An overview of how lobster-doxygen fits into the LOBSTER toolchain:
![lobster-doxygen in LOBSTER toolchain](doc/architecture/toolchain.png)

## Installation

- `git clone https://github.com/NewTec-GmbH/lobster-doxygen.git` to clone repository.
- `cd lobster-doxygen` to go to root directory.
- It is recommended to use a virtual environment:
  - In VS-Code: `Ctrl+Shift+P` type **Python: Create Environment**: select `Venv`.
    - When asked, select the Python version you want to work with, based on the versions installed in your machine.
    - When asked, select `dev` to be installed. This will set-up the development environment, including all the tools used in this template.
    - In the background, VS Code will install all the dependencies. This may take some time.
    - To activate the virtual environment, close all terminal panels inside of VS-Code.
      You can double check if the virtual environment is active, e.g. by `pip -V` the displayed path should point to your virtual environment.
  - In PowerShell:
    - `python -m venv .venv` to create the virtual environment.
    - `.venv\Scripts\Activate.ps1` to activate it.
    - `pip install -e .` to install required packages.
    - `pip install -e .[dev]` to install additional packages for development.
  - Under Linux / MacOS:
    - `python -m venv .venv` to create the virtual environment.
    - `source .venv/bin/activate` to activate it.
    - `pip install -e .` to install required packages.
    - `pip install -e .[dev]` to install additional packages for development.
  For more details about handling Venv, see [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv#Python_venv_activation)

## Usage

lobster-doxygen is a command line application that is configured via command line arguments.

```bash
usage: lobster-doxygen [-h] [-o OUTPUT] [-v] doxygen_folder

Script to generate the lobster common interchange format from a doxygen XML output.

positional arguments:
  doxygen_folder       Path to the doxygen XML output folder.

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Output file name.
  -v, --verbose        Enable verbose output.
```

## Doxygen XML files

In order to feed lobster-doxygen with the correct data, Doxygen needs to be configured.
For the requirement annotation the `Doxyfile` needs the following aliases:

```bash
ALIASES                = "implements{1}=@xrefitem implements \"Implements\" \"Requirement Traceability\" Requirement: \1" \
                         "justification{1}=@xrefitem justified \"Justified\" \"Justification Overview\" Justification: \1"
```

Change extract settings that Doxygen will use all entities in documentation:

```bash
EXTRACT_ALL            = YES
```

```bash
EXTRACT_PRIVATE        = YES
```

```bash
EXTRACT_PRIV_VIRTUAL   = YES
```

```bash
EXTRACT_PACKAGE        = YES
```

```bash
EXTRACT_STATIC         = YES
```

To enable the XML output:

```bash
GENERATE_XML           = YES
```

Once doxygen has run successfully, the `xml` directory can be set as the `doxygen_folder` in the application.
Example `Doxyfile` can be found in the [examples](./examples) directory.

## Examples

Check out the all the [Examples](./examples).

## SW Documentation

More information on the deployment and architecture can be found in the [documentation](./doc/README.md)

For Detailed Software Design run `$ /doc/detailed-design/make html` to generate the detailed design documentation that then can be found
in the folder `/doc/detailed-design/_build/html/index.html`

## Used Libraries

Used 3rd party libraries which are not part of the standard Python package:

| Library | Description | License |
| ------- | ----------- | ------- |
| [toml](https://github.com/uiri/toml) | Parsing [TOML](https://en.wikipedia.org/wiki/TOML) | MIT |
| [bmw-lobster](https://github.com/bmw-software-engineering/lobster)| | GPLv3 |
| [doxmlparser](https://github.com/doxygen/doxygen) | Parsing Doxygen XML | GPLv2 |
| [colorama](https://pypi.org/project/colorama/) | Console output color | BSD |

---
Sections below, for Github only

## Issues, Ideas And Bugs

If you have further ideas or you found some bugs, great! Create an [issue](https://github.com/NewTec-GmbH/lobster-doxygen/issues) or if you are able and willing to fix it by yourself, clone the repository and create a pull request.

## License

The whole source code is published under [GNU General Public License Version 3](https://github.com/NewTec-GmbH/lobster-doxygen/blob/main/LICENSE).
Consider the different licenses of the used third party libraries too!

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
