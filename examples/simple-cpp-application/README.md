# simple-cpp-application

This is an example of a C++ application to generates Doxygen XML output for the lobster-doxygen tool.

## Preparation

- In Windows:
  - Download Doxygen from https://www.doxygen.nl/index.html and add executable to system path.
- Under Linux / MacOS:
  - Install doxygen with package manager like `apt install doxygen`

## XML Output generation

- `doxygen` to generate XML output.
- `lobster-doxygen -v -o .\out\sw_test_result-lobster.json .\out\xml` to generate LOBSTER common interchange format file.
