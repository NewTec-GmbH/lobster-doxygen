# lobster-doxygen <!-- omit in toc -->

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://choosealicense.com/licenses/gpl-3.0/) [![Repo Status](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip) [![CI](https://github.com/NewTec-GmbH/lobster-doxygen/actions/workflows/test.yml/badge.svg)](https://github.com/NewTec-GmbH/lobster_doxygen/actions/workflows/test.yml)

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [SW Documentation](#sw-documentation)
- [Used Libraries](#used-libraries)
- [Issues, Ideas And Bugs](#issues-ideas-and-bugs)
- [License](#license)
- [Contribution](#contribution)

## Overview

Script to generate the lobster common interchange format from a doxygen XML output.

## Installation

```bash
git clone https://github.com/NewTec-GmbH/lobster-doxygen.git
cd lobster_doxygen 
pip install .
```

## Usage

>TODO

```bash
lobster_doxygen [-h] [-v] {command} {command_options}
```

Detailed descriptions of arguments

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

see also [requirements.txt](requirements.txt)

---
Sections below, for Github only

## Issues, Ideas And Bugs

If you have further ideas or you found some bugs, great! Create an [issue](https://github.com/NewTec-GmbH/lobster_doxygen/issues) or if you are able and willing to fix it by yourself, clone the repository and create a pull request.

## License

The whole source code is published under [GNU General Public License Version 3](https://github.com/NewTec-GmbH/lobster-doxygen/blob/main/LICENSE).
Consider the different licenses of the used third party libraries too!

## Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, shall be licensed as above, without any additional terms or conditions.
