/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @ingroup foo_group
 @file Foo.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <cstdlib>
#include <iostream>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES ******************************************************************************************/

/* PROTOTYPES *************************************************************************************/

static void foo1(void);
static void foo2(void);
/**
 * This function is for justification in prototype. 
 *
 * @justification{foo3 justification} 
 */
static void foo3(void);

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

extern void Foo_foo(void)
{
    std::cout << "foo";
    foo1();
    foo2();
}

/* INTERNAL FUNCTIONS *****************************************************************************/

/**
 * This function is for requirement in function. 
 *
 * @implements{SwRequirements.sw_req_foo1}
 */
static void foo1(void)
{
    std::cout << "foo1";
}

/**
 * This function is for justification in function. 
 *
 * @justification{foo2 justification} 
 */
static void foo2(void)
{
    std::cout << "foo2";
}

static void foo3(void)
{
    std::cout << "foo3";
}
