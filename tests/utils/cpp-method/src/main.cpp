/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @defgroup main_group Main file
 @file main.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

#include <iostream>

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

class Game 
{
public:
    /**
     * @brief Game constructor
     */
    Game(void) 
    {
        /* Nothing to to*/
    }

    /**
     * @brief Public method 
     * 
     * @implements{SwRequirements.sw_req_public_method}
     */
    void public_method(void)
    {

    }
protected:
    /**
     * @brief Protected method
     * 
     * @implements{SwRequirements.sw_req_protected_method}
     */
    void protected_method(void)
    {
    }
private:
    /**
     * @brief Private method
     * 
     * @implements{SwRequirements.sw_req_private_method}
     */
    void private_method(void)
    {
    }
};

class Foo
{
public:
    /**
     * @brief Game constructor
     */
    Foo(void) 
    {
        /* Nothing to to*/
    }

    /**
     * @brief Public method 
     * 
     * @justification{Public method justification}
     */
    void public_method(void)
    {

    }
protected:
    /**
     * @brief Protected method
     * 
     * @justification{Protected method justification}
     */
    void protected_method(void)
    {
    }
private:
    /**
     * @brief Private method
     * 
     * @justification{Private method justification}
     */
    void private_method(void)
    {
    }
};

/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

int main(void)
{
    return EXIT_SUCCESS; 
}
