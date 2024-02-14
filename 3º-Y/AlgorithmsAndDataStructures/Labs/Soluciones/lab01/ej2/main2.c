#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/* Maximum allowed length of the array */
#define MAX_SIZE 100000


unsigned int array_from_stdin(int array[],unsigned int max_size){
    unsigned int length, i;
    
    //get array lenght
    printf("Specify array length:");
    scanf("%u",&length);
    
    if(length>max_size || length<=0){
        printf("Error: Invalid array length. Must be between 1 and 100000\n");
        exit(EXIT_FAILURE);
    }
    
    //get array elements
    for(i=0;i<length;i++){
        printf("Ingrese el elemento %uº del array:",i+1);
        scanf("%d",&array[i]); 
    }

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


int main(void){
 
    /* create an array of MAX_SIZE elements */
    int array[MAX_SIZE];
    
    /* parse the file to fill the array and obtain the actual length */
    unsigned int length = array_from_stdin(array, MAX_SIZE);
    
    /*dumping the array*/
    array_dump(array, length);
    
    return EXIT_SUCCESS;
}
