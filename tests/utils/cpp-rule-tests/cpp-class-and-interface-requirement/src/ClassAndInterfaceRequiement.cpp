/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @defgroup class_and_interface_requirement_group Class and interface requirements
 @file ClassAndInterfaceRequirement.cpp
***************************************************************************************************/

/* INCLUDES ***************************************************************************************/

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES AND CLASSES ******************************************************************************/

/**
 * @brief Counter
 * 
 * Interface class to test requirements in class and interface level
 * 
 * @implements{SwRequirements.sw_req_class}
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
     * @implements{SwRequirements.sw_req_interface_method}
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
