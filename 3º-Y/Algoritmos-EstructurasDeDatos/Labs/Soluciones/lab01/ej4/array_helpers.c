#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "array_helpers.h"

unsigned int array_from_file(int array[],unsigned int max_size,const char *filepath){
    int a;
    unsigned int length, i;
    FILE *f;

    f=fopen(filepath, "r");
    
    //get array lenght
    fscanf(f,"%u",&length);
    
    if(length>max_size || length<=0){
        printf("Error: Invalid array length.\n");
        exit(EXIT_FAILURE);
    }
    
    //get array elements
    for(i=0;i<length;i++){
        //Si existe elemento retorna 1 sino -1. Además se guarda en elemento en el array
        a=fscanf(f,"%d",&array[i]); 
        
        if(a==-1){
            printf("Error: Missing array element(s) acording its length.\n");
            exit(EXIT_FAILURE);
        }
    }

    fclose(f);

    return length;
}

void array_dump(int a[], unsigned int length) {
    unsigned int i;
    printf("[");
    for(i=0; i<length-1; i++){
        printf(" %d,", a[i]);
    }
    //Lo printeo aparte para tener las comas en las posiciones adecuadas
    printf(" %d",a[length-1]);
    printf("]\n");
}
bool array_is_sorted(int a[], unsigned int length){
    unsigned int i=0;
    bool sorted=true;
    
    while(i<length-1 && sorted){
        if (a[i]>a[i+1]){
            sorted=false;
        }
        i+=1;
    }
    return sorted;
}