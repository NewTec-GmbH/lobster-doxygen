/***************************************************************************************************
lobster-doxygen - Doxygen XML to LOBSTER common interchange format converter
Copyright (c) NewTec GmbH 2025   -   www.newtec.de

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
***************************************************************************************************/
/**
 @defgroup class_and_method_requirement_group Class an method requirement
 @file ClassAndMethodRequirement.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <stdint.h>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * @brief Counter
 * 
 * Class to test requirements class and method level
 * 
 * @implements{SwRequirements.sw_req_class}
 */
class Counter {
public:
    /**
     * @brief Construct a new Counter object
     * @implements{SwRequirements.sw_req_class_method}
     */
    Counter(void);
};

/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

Counter::Counter(void) 
{
  /* Nothing to do. */
}
