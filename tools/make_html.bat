@ECHO OFF
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

setlocal

set ONLINE_REPORT_OPTION=""

if "%~1"=="" (
    REM No arguments provided, proceed normally.
) else if "%~1"=="online" (
    set ONLINE_REPORT_OPTION="online"
) else (
    echo Error: Invalid argument "%~1". Only optional "online" is allowed. >&2
    exit /b 1
)

REM Create reStructured Text documentation from TRLC models and files.
call trlc2other/make_rst

REM Create unit test reports
call testReport/make_rst 

REM Create tracing report from TRLC and source files.
call traceReport/make %ONLINE_REPORT_OPTION%

REM Create HTML documentation.
call deployDoc/make html

endlocal