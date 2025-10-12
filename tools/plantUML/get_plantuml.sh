#!/bin/bash
# lobster-doxygen - Doxygen XML to LOBSTER common interchange format converter
# Copyright (c) NewTec GmbH 2025   -   www.newtec.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

DIR=$(dirname `realpath "$_"`)
PLANTUML="$DIR/plantuml.jar"
export PLANTUML

if [ ! -f "$PLANTUML" ]; then
    echo "Download PlantUML java program..."
    curl -L -o "$PLANTUML" https://github.com/plantuml/plantuml/releases/download/v1.2024.8/plantuml-1.2024.8.jar
fi
