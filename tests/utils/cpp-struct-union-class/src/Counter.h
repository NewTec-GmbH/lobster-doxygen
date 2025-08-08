/***************************************************************************************************
  (c) NewTec GmbH 2025   -   www.newtec.de
***************************************************************************************************/
/**
 @ingroup main_group 
 @defgroup counter_group counter module 

 @brief Counter module 

 Module with counter class.

 @file Counter.h
***************************************************************************************************/
#ifndef COUNTER_H
#define COUNTER_H

#ifdef __cplusplus
extern "C"
{
#endif

/* INCLUDES ***************************************************************************************/

/* CONSTANTS **************************************************************************************/

/* MACROS *****************************************************************************************/

/* TYPES ******************************************************************************************/

/* PROTOTYPES *************************************************************************************/

/**
 * @brief Counter
 * 
 * Class to test requirements and justification in class level
 * 
 * @implements{SwRequirements.sw_req_counter_class}
 */
class Counter {
public:
    /**
     * @brief Construct a new Counter object
     * 
     */
    Counter(void);

    /**
     * @brief Getter for counter value
     */
    int get_counter(void);

    /**
     * @brief Count up
     */
    void count_up(void);
private:
    /** 
     * @brief Internal counter value 
     */
    int counter = 0; 
};

#ifdef __cplusplus
}
#endif

#endif  /* COUNTER_H */
