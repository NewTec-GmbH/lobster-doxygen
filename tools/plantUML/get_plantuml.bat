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

setlocal
set LOCAL_DIR=%~dp0
endlocal & (
    set PLANTUML=%LOCAL_DIR%plantuml.jar
)

if not exist "%PLANTUML%" (
    echo Download PlantUML java program...
    powershell -Command "Invoke-WebRequest https://github.com/plantuml/plantuml/releases/download/v1.2024.8/plantuml-1.2024.8.jar -OutFile %PLANTUML%"
)
