/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
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
