#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>
#include "stack.h"

int main(){

    stack s=stack_empty();

    s=stack_push(s,1);
    s=stack_push(s,2);
    printf("Top elem: %d\n",stack_top(s));
    
    s=stack_pop(s);
    printf("Top elem after pop: %d\n",stack_top(s));

    for(unsigned int i=2;i<=10;i++){
        s=stack_push(s,i);
    }
    printf("Stack size:%u\n",stack_size(s));

    stack_elem *array;
    array=stack_to_array(s);
    printf("[");
    for(unsigned int i=0;i<10;i++){
        printf("%d",array[i]);
        if(i!=9){
            printf(",");
        }
    }
    printf("]\n");
    free(array);

    // array of empty stack 
    stack p=stack_empty();
    stack_elem *arr2;
    arr2=stack_to_array(p);
    printf("%d",arr2[3]); //it prints 0
    
    free(p);
    return EXIT_SUCCESS;
}