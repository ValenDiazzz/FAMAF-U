#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

#include "counter.h"

struct _counter {
    unsigned int count;
};

counter counter_init(void) {
    counter c;
    c=malloc(sizeof(struct _counter));
    c->count=0;
    return c;   
}

void counter_inc(counter c) {
    c->count++;
}

bool counter_is_init(counter c) {
    return c->count==0;
}

void counter_dec(counter c) {
    if (counter_is_init(c)) {
        printf("Counter has initial value");
        exit(EXIT_FAILURE);
    }else{
        c->count--;
    }
}

counter counter_copy(counter c) {
    counter q;
    q=malloc(sizeof(struct _counter));
    q->count=c->count;
    return q;
}

void counter_destroy(counter c) {
    free(c);
    c=NULL;
}
