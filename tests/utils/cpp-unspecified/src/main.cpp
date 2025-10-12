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
 @defgroup main_group Main file
 @file main.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <cstdlib>
#include <iostream>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * Struct with no requirement or justification 
 */
typedef struct {
    int number;
} struct_t;

/**
 * Union with no requirement or justification
 */
typedef union {
    int number_1;
    int number_2;
}union_t;

/**
 * Class with no requirement or justification 
 */
class Counter {
public:
    /**
     * Constructor method with no requirement or justification 
     */
    Counter(void){
        /* Empty constructor */
    }

    /**
     * Interface with no requirement or justification
     */
    virtual void count_up(void) = 0;
};


/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

/**
 * Function with no requirement or justification 
 */
void function(void)
{
    /* Empty function */
}

/**
 * Namespace with no requirement or justification 
 */
namespace math
{ 
    int add(int val1, int val2)
    {
        return val1 + val2;
    }
} 


int main(void)
{
    return EXIT_SUCCESS; 
}
