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

rem Keep all environment variables local to this script.
setlocal

set TRLC_CONVERTER=pyTRLCConverter
set OUTPUT_DIR=out
set CONVERTER=converter/req2markdown.py
set TRANSLATION=converter/translation.json
set OUT_FORMAT=markdown

if not exist "%OUTPUT_DIR%" (
    md %OUTPUT_DIR%
) else (
    del /q /s "%OUTPUT_DIR%\*" >nul
)

%TRLC_CONVERTER%  --source=..\..\trlc\swe-req --include=..\..\trlc\model --verbose --out=%OUTPUT_DIR% --project=%CONVERTER% --translation=%TRANSLATION% %OUT_FORMAT%

if errorlevel 1 (
    goto error
)

%TRLC_CONVERTER%  --source=..\..\trlc\swe-arch --include=..\..\trlc\model --include=..\..\trlc\swe-req --exclude=..\..\trlc\swe-req --verbose --out=%OUTPUT_DIR% --project=%CONVERTER% --translation=%TRANSLATION% %OUT_FORMAT%

if errorlevel 1 (
    goto error
)

set CONVERTER=converter/tc2markdown.py

%TRLC_CONVERTER%  --source=..\..\trlc\swe-test --include=..\..\trlc\model --include=..\..\trlc\swe-req --exclude=..\..\trlc\swe-req --verbose --out=%OUTPUT_DIR% --project=%CONVERTER% --translation=%TRANSLATION% %OUT_FORMAT%

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