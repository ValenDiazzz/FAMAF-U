#include "strfuncs.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

size_t string_length(const char *str){
    size_t length=0;
    while(str[length]!='\0'){
        length++;
    }
    return length;
}

char *string_filter(const char *str, char c){
    size_t str_len=string_length(str);
    char *d_str=NULL;
    d_str=malloc((sizeof(char)*str_len)+1); //Le sumo 1 por el "\0"

    unsigned int j=0;
    for(unsigned int i=0;str[i]!='\0';i++){
        if(str[i]!=c){
            d_str[j]=str[i];
            j++;
        }
    }
    d_str[j+1]='\0';
    return d_str;
}