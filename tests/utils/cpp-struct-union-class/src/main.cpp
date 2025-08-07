/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @defgroup main_group Main file
 @file main.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <iostream>
#include <stdint.h>
#include "Counter.h"

/* CONSTANTS **************************************************************************************/

using namespace std;

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * @brief Numbers struct
 * 
 * @implements{SwRequirements.sw_req_numbers_struct}
 */
typedef struct {
    uint16_t number_1;
    uint16_t number_2;
} numbers_t;

/**
 * @brief Memory struct
 * 
 * @implements{SwRequirements.sw_req_memory_union}
 */
typedef union {
    numbers_t numbers;
    uint32_t number;
}memory_t;

/**
 * @brief Foo class
 * 
 * @justification{class justification}
 */
class FooClass {
public:
    FooClass(void){
        
    }
};

/**
 * @brief Foo stuct
 * 
 * @justification{struct justification}
 */
typedef struct {
    uint32_t number;
}foo_t;

/**
 * @brief Foo union
 * 
 * @justification{union justification}
 */
typedef union{
    uint32_t number;
    uint32_t same_number;
}numbers_u;

/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

int main(void)
{
    Counter counter;
    counter.count_up();
    cout << counter.get_counter() << "\n";

    numbers_t numbers = {.number_1 = 1, .number_2 = 2};
    cout << "number.number_1 = " << numbers.number_1 << "\n";

    memory_t memory = {.number = 0xFFFF};
    cout << "memory.numbers.number_1 = " << memory.numbers.number_1 << "\n" ;

    return EXIT_SUCCESS; 
}
