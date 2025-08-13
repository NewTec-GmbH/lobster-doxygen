/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
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
