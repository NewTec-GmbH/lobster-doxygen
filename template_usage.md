# Python Template User Guide <!-- omit in toc -->

- [Install Template](#install-template)
- [Usage with VS Code](#usage-with-vs-code)
- [Handling dependencies](#handling-dependencies)
- [Starting Implementation](#starting-implementation)
- [Package installation](#package-installation)
  - [For development](#for-development)
  - [Current Version from source](#current-version-from-source)
- [Folder Structure](#folder-structure)
- [Documentation](#documentation)
  - [High level SW Architecture](#high-level-sw-architecture)
  - [Detailed Design](#detailed-design)
- [Unit Testing](#unit-testing)
- [Github](#github)
  - [Github Work Instructions](#github-work-instructions)
  - [Github Workflow](#github-workflow)

## Install Template

- In GitHub, use the button `Use this template` to create a new repository.
- When not using GitHub, copy template repository.
- Rename the folder `src/template_python` to your desired package name.
- Rename the file `template_python.py` to your desired package name.
- Adapt the imports in the former `template_python.py`:

```python
from <your_project_name>.version import __version__, __author__, __email__, __repository__, __license__
```

- Change the author, email and description in `pyproject.toml`.
- Update the sections `[project.urls]` and `[projects.scripts]` in `pyproject.toml`.
- Update the README file in root folder.
- This are only the most important places where to update the template, use search and replace, to find all occurances of `template_python`and replace it by you project name.

## Usage with VS Code

- To install the recommended extensions if desired, use "Open Workspace from File" and open `.vscode\python.code-workspace` then you will be asked if you would like to install the recommended extensions.

- For creating of new files, use the provided templates. To use them just start typing "template" in a new file and select the template you need.

It is recommended to use a virtual environment for each Python project e.g. Venv.

- In VS-Code: `Ctrl+Shift+P` type **Python: Create Environment**: select `Venv`.
  - When asked, select the Python version you want to work with, based on the versions installed in your machine.
  - When asked, select `requirements-dev.txt` to be installed. This will set-up the development environment , including all the tools used in this template.
  - In the background, VS Code will install all the dependencies. This may take some time.
  - To activate the virtual environment, close all terminal panels inside of VS-Code.
    You can double check if the virtual environment is active, e.g. by `pip -V` the displayed path should point to your virtual environment.
- In PowerShell:
  - `python -m venv .venv` to create the virtual environment.
  - `.venv\Scripts\Activate.ps1` to activate it.
- Under Linux / MacOS:
  - `python -m venv .venv` to create the virtual environment.
  - `source myvenv/bin/activate` to activate it.
For more details about handling Venv, see [Python venv: How To Create, Activate, Deactivate, And Delete](https://python.land/virtual-environments/virtualenv#Python_venv_activation)

For more details see [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) and [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).

## Handling dependencies

Before starting with the development, install all necessary dependencies from [requirements-dev.txt](requirements-dev.txt): `pip install -r requirements-dev.txt`.
This are the dependencies necessary for development only.
When additional packages are necessary for development add them to requirements-dev.txt.

When additional dependencies are necessary for the Python package under development during runtime:

- add dependencies to `pyproject.toml` in the dependencies section.
- provide a `requirements.txt` that includes all this dependencies.

To find all used dependencies, you can use `pipreqs --force`. This will overwrite the existing requirements.txt with an updated version containing all used packages.
In contrast to pip freeze >requirements.txt, this will only include the used packages, but not their dependencies, and not the installed packages. This can help to prevent version conflicts in dependencies.
For more information see [stop using pip freeze](https://builtin.com/software-engineering-perspectives/pip-freeze)

## Starting Implementation

Before starting to implement your Python package check the [coding guidelines](coding-guidelines/README.md).

## Package installation

Before installing, double-check that all information in [pyproject.toml](pyproject.toml) is up to date, especially:

- Version Information
- Dependencies

### For development

Install as editable package, run in root folder: `pip install -e .`

This generates a link only, pointing to the package located under `/src`

### Current Version from source

Run in root folder:

```cmd
pip install .

### Build a wheel for distribution

To build a Python wheel for distribution, run in root folder `pip wheel -w ./dist --no-deps ./`. To install the wheel just run `pip install template_python.whl` with the generated wheel file.

### Compile into an executable

It is possible to create an executable file that contains the package and all its dependencies. "PyInstaller" is used for this. If not already installed: `pip install pyinstaller`

Run the following command in the root folder:

```cmd
pyinstaller --noconfirm --onefile --console --name "template_python" --add-data "./pyproject.toml;."  "./src/template_python/templaty_python.py"
```

## Folder Structure

This sections describes the most important folders of the template

```md
root
├── .github -> delete when not using github
│   └── workflows -> Add your Git continous integration workflows here
├── .vscode -> Settings for VS-Code, delete if VS-Code is not used (not reccomended)
│   ├── python.code-workspace -> contains recomended plugins for VS-Code
│   ├── settings.json -> useful settings for some plugins
│   └── template_xxx.code-snippets -> some useful code snippets
├── coding-guidelines -> Python Coding Guidelines to be used for this project
├── dist -> output folder for generated binaries
├── doc -> contains package documentation
│   ├── detailed-design -> prepared Sphinx setup for code documentation based on docstrings
│   │   ├── conf.py -> Sphinx configuration
│   │   ├── index.rst -> documentation frontpage. Customize for project needs
│   │   └── make.bat -> call make html to generate documentation
│   └── README.md -> High level SW architecture
├── examples -> describe examples how to use the package if not in root/README.md
├── src
│   └── template_python -> package name, rename to project name
│       ├── __init__.py -> Mark folder as python package
│       ├── template_python.py -> contains main function, rename to project name
│       └── version.py -> extracts version info from metadata for use in implementation
├── tests -> implements unit tests here
├── .gitattributes -> defines some file extension handling, delete if Git is not used
├── .gitignore -> rules to ignore files for commit, delete if Git is not used
├── .pylintrc -> configuration for PyLint according to coding guidelines
├── LICENSE -> customize for project, add detailed license information here
├── pyproject.toml -> configuration for packaging of Python package with Pip
├── README.md -> main readme file, customize for project
├── requirements.txt -> contains all dependencies, customize for project
└── template_usage.md -> this file

```

## Documentation

### High level SW Architecture

Add a high level SW Architecture documentation to [doc/README.md](doc/README.md). Usually this is done by using the following UML diagrams:

- Component diagram for modeling the context.
- For tools that deals with different servers / machines, also document the deployment.
- Use Case diagram to describe the main use cases.
- Class diagram to describe the used clases and their interfaces.
- Sequence chart and/or state machines for describing the dynamic behavior.

For modeling these diagrams, use PlantUML sections in the README.md, These diagrams are rendered by sphinx when generating the design documents, as well as in VS-Code Markdown preview, if PlantUML extension is installed.

The Sphinx `make.bat` will copy all `.md` files located in `/doc` to `/doc/detailed-design/_sw-architecture/` so that they can be included e.g. by `index.rst`.

Markdown files included by Sphinx are interpreted by [MyST Parser](https://myst-parser.readthedocs.io/en/latest/).

### Detailed Design

In this template, Sphinx already is set-up and configured.

The starting point of the detailed design is [index.rst](doc/detailed-design/index.rst).
This file is updated automatically by a script when generating the the detailed design as described below,
with informations from the project. If you want to edit there something by your own, maybe `update_doc_from_source.py`
needs to be updated as well.

The following steps show how to generate a source code documentation similar to Doxygen, based on Python Docstring:

- Customize `/doc/detailed-design/conf.py`:
  - update the path to your source code.
  - update the project information.
  - update path to your local `plantuml.jar` file or rendering server.
- run `doc/detailed-design/make.bat html`.
- generated documentation can be found in [doc/detailed-design/_build/html](doc/detailed-design/_build/html/index.html).
- if a python file under `/src` was deleted or renamed, delete the folder `/doc/detailed-design/_autosummary`.

## Unit Testing

Unit Testing setup is prepared in the folder `/tests`, from there you can run the tests e.g. by `pytest ./ -v --cov=../src --cov-report=term-missing`
The [How-to Guides](https://docs.pytest.org/en/stable/how-to/index.html) of pytest are a good entry point on how to do unit testing with pytest

## Github

### Github Work Instructions

Detailed instructions for working with GitHub for NewTec projects are available at [gitWorkInstructions](https://newtec-gmbh.github.io/gitWorkInstructions/)

### Github Workflow

A example workflow is prepared in the folder `.github/workflows`, the `test.yml` is prepared to execute PyLint and run the unit tests located in `/tests`.
