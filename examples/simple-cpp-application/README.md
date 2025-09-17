# simple-cpp-application

This is an example of a C++ application to generates Doxygen XML output for the lobster-doxygen tool.

## Preparation

- In Windows:
  - Download Doxygen from https://www.doxygen.nl/index.html and add executable to system path.
- Under Linux / MacOS:
  - Install doxygen with package manager like `apt install doxygen`

## XML Output generation

Call `doxygen` to generate XML output.

## XML conversion to LOBSTER interchange format

Call `lobster-doxygen --verbose --output ./out/sw_test_result-lobster.json ./out/xml` to generate the LOBSTER common interchange format file.

THis will create the file ```out/sw_test_result-lobster.json``` containing the trace information from the source code.