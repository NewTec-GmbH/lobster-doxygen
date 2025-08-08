/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @ingroup function_prototype_group
 @file FunctionPrototype.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <cstdlib>
#include <iostream>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/* PROTOTYPES *************************************************************************************/

static void foo1(void);
static void foo2(void);
/**
 * This function is for justification in prototype. 
 *
 * @justification{Prototype justification} 
 */
static void foo3(void);

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

extern void FunctionPrototype_foo(void)
{
    std::cout << "foo";
    foo1();
    foo2();
}

/* INTERNAL FUNCTIONS *****************************************************************************/

/**
 * This function is for requirement in function. 
 *
 * @implements{SwRequirements.sw_req_function}
 */
static void foo1(void)
{
    std::cout << "foo1";
}

/**
 * This function is for justification in function. 
 *
 * @justification{Function justification} 
 */
static void foo2(void)
{
    std::cout << "foo2";
}

static void foo3(void)
{
    std::cout << "foo3";
}
