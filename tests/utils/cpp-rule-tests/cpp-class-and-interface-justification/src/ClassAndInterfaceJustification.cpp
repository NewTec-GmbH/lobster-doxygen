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
