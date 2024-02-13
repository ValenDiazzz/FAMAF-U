/*
@file array_helpers.c
@brief Array Helpers method implementation
*/
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "array_helpers.h"

/**
* @brief returns true when reach last line in prices file
* @return True when is the last line of the file, False otherwise
*/
static bool is_last_line(unsigned int store) {
  return store == STORES - 1u;
}

void array_dump(PricesTable a) {
  for (unsigned int store = 0u; store < STORES; ++store) {
      Store sp = a[store][price];
      Store sd = a[store][discount];
      fprintf(stdout, "store %c %u: Potato: %u (%u), Cabbage: %u (%u), Carrot: %u (%u), Onion: %u (%u), Radish: %u (%u)",
                      sp.code, sd.index,
                      sp.potatoes, sd.potatoes,
                      sp.cabbages, sd.cabbages,
                      sp.carrots, sd.carrots,
                      sp.onions, sd.onions,
                      sp.radishes, sd.radishes
                    );
      if (!is_last_line(store))
      {
        fprintf(stdout, "\n");
      }
    }
}

unsigned int best_relative_price (PricesTable a) {
  unsigned int min_price,total_price,ste; 
  Store ste_pr,ste_disc;
  min_price=UINT_MAX;

  for(ste=0;ste<STORES;ste++){
    ste_pr=a[ste][price];
    ste_disc=a[ste][discount];
    
    total_price=((ste_pr.potatoes*(100-ste_disc.potatoes)) + 
                (ste_pr.cabbages*(100-ste_disc.cabbages))+
                (ste_pr.carrots*(100-ste_disc.carrots))+
                (ste_pr.onions*(100-ste_disc.onions))+
                (ste_pr.radishes*(100-ste_disc.radishes)))/100;
    
    if(total_price<min_price){
      min_price=total_price;
    }
  }
  return min_price;
}

void array_from_file(PricesTable array, const char *filepath) {
  FILE *file = NULL;

  file = fopen(filepath, "r");
  if (file == NULL) {
    fprintf(stderr, "File does not exist.\n");
    exit(EXIT_FAILURE);
  }

  char code;
  unsigned int index;

  int i = 0;
  while (!feof(file)) { 
    int res = fscanf(file," _%c_%u_ ",&code, &index); 
    if (res != 2) {
      fprintf(stderr, "Invalid file.\n");
      exit(EXIT_FAILURE);
    }
   
    Store store_prices = store_from_file(file, code, price, index);
    Store store_discounts = store_from_file(file, code, discount, index);

    array[index-1][price]=store_prices;
    array[index-1][discount]=store_discounts;
    i++;
  }
  fclose(file);
}

