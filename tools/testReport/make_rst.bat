@echo off
REM lobster-doxygen - Doxygen XML to LOBSTER common interchange format converter
REM Copyright (c) NewTec GmbH 2025   -   www.newtec.de
REM
REM This program is free software: you can redistribute it and/or modify
REM it under the terms of the GNU General Public License as published by
REM the Free Software Foundation, either version 3 of the License, or
REM (at your option) any later version.
REM
REM This program is distributed in the hope that it will be useful,
REM but WITHOUT ANY WARRANTY; without even the implied warranty of
REM MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM GNU General Public License for more details.
REM
REM You should have received a copy of the GNU General Public License
REM along with this program.  If not, see <https://www.gnu.org/licenses/>.

rem Store the current directory on the stack and change to the directory of this script.
rem This allows the script to be run from any directory.
rem The script will always use the directory where it is located as the working directory.
pushd %~dp0

pushd ..\plantUML
call get_plantuml.bat
popd

setlocal

set SRC_PATH=./src
set TESTS_PATH=./tests
set COVERAGE_REPORT=coverage
set REPORT_TOOL_PATH=%~dp0
set TEST_RESULT_REPORT_XML=sw_test_result_report.xml
set TEST_RESULT_REPORT_TRLC=sw_test_result_report.trlc
set TRLC_CONVERTER=pyTRLCConverter
set CONVERTER_DIR=../trlc2other/converter
set OUTPUT_DIR=out
set CONVERTER=%CONVERTER_DIR%/create_test_report_in_rst.py
set OUT_FORMAT=rst

if not exist "%OUTPUT_DIR%" (
    md %OUTPUT_DIR%
) else (
    del /q "%OUTPUT_DIR%\*" >nul
)

rem Create the sw test report and the coverage analysis.
pushd  ..\..
pytest %TESTS_PATH% -v --cov=%SRC_PATH% --cov-report=term-missing --cov-report=html:%REPORT_TOOL_PATH%/%OUTPUT_DIR%/%COVERAGE_REPORT% -o junit_family=xunit1 --junitxml=%REPORT_TOOL_PATH%/%OUTPUT_DIR%/%TEST_RESULT_REPORT_XML%
popd

if errorlevel 1 (
    goto error
)

rem Convert sw test report XML to TRLC.
python test_result_xml2trlc.py ./%OUTPUT_DIR%/%TEST_RESULT_REPORT_XML% ./%OUTPUT_DIR%/%TEST_RESULT_REPORT_TRLC%

if errorlevel 1 (
    goto error
)

rem Convert sw test report TRLC to reStructuredText.
%TRLC_CONVERTER% --source=..\..\trlc\swe-req --source=..\..\trlc\swe-test --source=..\..\trlc\model --exclude=..\..\trlc\swe-req --exclude=..\..\trlc\swe-test --source=%OUTPUT_DIR%\%TEST_RESULT_REPORT_TRLC% -o=%OUTPUT_DIR% --project=%CONVERTER% --verbose %OUT_FORMAT%

if errorlevel 1 (
    goto error
)

goto finished

:error

:finished

endlocal
rem Restore the previous directory from the stack.
rem This allows the script to return to the original working directory.
popd