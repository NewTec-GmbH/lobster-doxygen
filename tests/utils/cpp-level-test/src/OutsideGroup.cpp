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
 @file OutsideGroup.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <iostream>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * This struct is for no group justification.
 *  
 * @justification{No group struct justification}
 */
typedef struct {
    int number;      
} no_group_struct_t;

/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

/**
 * This function is for requirement in no group function. 
 *
 * @implements{SwRequirements.sw_req_no_group_function}
 */
static void no_group_function(void)
{
    std::cout << "no doxygen group function";
}
