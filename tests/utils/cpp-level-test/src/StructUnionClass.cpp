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
 @ingroup struct_union_class_group
 @file StructUnionClass.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <stdint.h>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * @brief Numbers struct
 * 
 * @implements{SwRequirements.sw_req_struct}
 */
typedef struct {
    uint16_t number_1;
    uint16_t number_2;
} numbers_t;

/**
 * @brief Memory struct
 * 
 * @implements{SwRequirements.sw_req_union}
 */
typedef union {
    numbers_t numbers;
    uint32_t number;
}memory_t;

/**
 * @brief Counter
 * 
 * Class to test requirements and justification in class level
 * 
 * @implements{SwRequirements.sw_req_class}
 */
class Counter {
public:
    /**
     * @brief Construct a new Counter object
     * 
     */
    Counter(void);
};

/**
 * @brief Foo class
 * 
 * @justification{Class justification}
 */
class FooClass {
public:
    FooClass(void){
        
    }
};

/**
 * @brief Foo stuct
 * 
 * @justification{Struct justification}
 */
typedef struct {
    uint32_t number;
}foo_t;

/**
 * @brief Foo union
 * 
 * @justification{Union justification}
 */
typedef union{
    uint32_t number;
    uint32_t same_number;
}numbers_u;


/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

Counter::Counter(void) 
{
  /* Nothing to do. */
}
