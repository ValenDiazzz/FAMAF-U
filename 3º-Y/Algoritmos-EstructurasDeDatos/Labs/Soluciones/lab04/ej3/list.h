#ifndef _LIST_H
#define _LIST_H
#include <stdbool.h>


typedef int list_elem;
typedef struct node_t *list;

//Constructors

list empty();
/*returns empty list*/

list addl(list l, list_elem e);
/*adds element at the beginning of the list*/


//Operations

list destroy(list l);
/*Frees memory for l*/

bool is_empty(list l);
/*returns true if the list is empty*/

list_elem head(list l);
/*returns the first element of the list
    PRECONDITION: !is_empty(l)
*/

list tail(list l);
/*Deletes the first element of the list
    PRECONDITION: !is_empty(l)
*/

list addr(list l, list_elem e);
/*adds element at the end of the list*/

unsigned int length(list l);
/*returns list length*/

list concat(list l1, list l2);
/*Concats lists l1 and l2 and store it in l1*/

list_elem index(list l, unsigned int i);
/*returns the i-th element of the list
    PRECONDITION: length(l)>i
*/

 void take(list l, unsigned int i);
/*deletes element its position are greater than i*/

void drop(list l, unsigned int i);
/*deletes element in the position i-th and backwards*/

list copy_list(list l1);
/*returns a copy of a list*/

#endif