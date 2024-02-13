#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>
#include "stack.h"

struct _s_stack {
    stack_elem *elems;      // Arreglo de elementos
    unsigned int size;      // Cantidad de elementos en la pila
    unsigned int capacity;  // Capacidad actual del arreglo elems
};

stack stack_empty(){
    stack s=malloc(sizeof(struct _s_stack));
    s->elems=malloc(sizeof(stack_elem));
    s->size=0;
    s->capacity=1;
    return s;
}

stack stack_push(stack s, stack_elem e){
    if(s->capacity == s->size){  //Si el arreglo esta lleno aumento capacidad.
        s->elems=realloc(s->elems, 2*s->capacity*sizeof(stack_elem));
        s->capacity*=2;
    }
    (s->elems)[s->size]=e;
    s->size++;
    return s;
}
stack stack_pop(stack s){
    if(s->size!=0){
        s->size--;
    }
    return s;
}
unsigned int stack_size(stack s){
    return s->size;
}

stack_elem stack_top(stack s){
    return s->elems[stack_size(s)-1];
}

bool stack_is_empty(stack s){
    return s->size==0;
}

stack_elem *stack_to_array(stack s){
    unsigned int len=stack_size(s);
    stack_elem *array=calloc(len,sizeof(stack_elem));
    for(unsigned int i=0;i<len;i++){
        array[i]=s->elems[i];
    } 
    return array;
}

stack stack_destroy(stack s){
    if(s!=NULL){
        free(s->elems);
        free(s);
        s=NULL;
    }
    return s;
}