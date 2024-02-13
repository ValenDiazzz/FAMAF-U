/*
@file array_helpers.c
@brief Array Helpers method implementation
*/
#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

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
  /* COMPLETAR */
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
  while (/* COMPLETAR */) {
    int res = fscanf(/* COMPLETAR */);
    if (res != 2) {
      fprintf(stderr, "Invalid file.\n");
      exit(EXIT_FAILURE);
    }
    /* COMPLETAR: Leer y guardar ambos Store en el array multidimensional*/
    Store store_prices = /* completar... */;
    Store store_discounts = /* completar... */;
    /* completar... */
    i++;
  }
  fclose(file);
}
