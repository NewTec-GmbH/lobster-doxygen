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
 @ingroup main_group 
 @defgroup function_prototype_group FunctionPrototype module 

 @brief Function prototype module 

 Module with functions and prototypes.

 @file FunctionPrototype.h
***************************************************************************************************/
#ifndef FUNCTION_PROTOTYPE_H
#define FUNCTION_PROTOTYPE_H

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
 * This function is for requirement in prototype. 
 * 
 * @implements{SwRequirements.sw_req_prototype}
 */
extern void FunctionPrototype_foo(void);

#ifdef __cplusplus
}
#endif

#endif  /* FUNCTION_PROTOTYPE_H */
