/*
  @file store.c
  @brief Implements store structure and methods
*/
#include <stdlib.h>
#include "store.h"

static const int AMOUNT_OF_STORE_VARS = 5;

Store store_from_file(FILE* file, char code, type_t type, unsigned int index)
{
    Store store;
    store.code=code;
    store.type=type;
    store.index=index;
    
    int res=fscanf(file, EXPECTED_PRICES_FILE_FORMAT,&store.potatoes ,&store.cabbages
                   ,&store.carrots ,&store.onions ,&store.radishes);
                   
    if(res!=AMOUNT_OF_STORE_VARS){
      fprintf(stderr,"Invalid array.\n");
      exit(EXIT_FAILURE);
    }
    return store;
}
