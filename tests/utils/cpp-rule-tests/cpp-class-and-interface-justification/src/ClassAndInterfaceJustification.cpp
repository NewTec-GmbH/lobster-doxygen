/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @defgroup class_and_interface_justification_group Class and interface justification
 @file ClassAndInterfaceJustification.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * @brief Counter
 * 
 * Interface class to test justification in class and interface level
 * 
 * @justification{Class justification}
 */
class ICounter {
public:
    /**
     * @brief Construct a new Counter object
     */
    ICounter(void);

    /**
     * @brief Count up
     * 
     * @justification{Interface method justification}
     */
    virtual void count_up(void) = 0;
};

/* PROTOTYPES *************************************************************************************/

/* VARIABLES **************************************************************************************/

/* EXTERNAL FUNCTIONS *****************************************************************************/

/* INTERNAL FUNCTIONS *****************************************************************************/

ICounter::ICounter(void) 
{
  /* Nothing to do. */
}
