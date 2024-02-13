#ifndef _STRFUNCS_H
#define _STRFUNCS_H

#include <stddef.h>
/**
* @brief Returns string length.
* @param str string
*/
size_t string_length(const char *str);


/**
* @brief Returns dynamic string which consists of the string str without the character c.
* @param str string
* @param c character
*/
char *string_filter(const char *str, char c);

#endif