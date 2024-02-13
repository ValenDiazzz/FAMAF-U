#include <stdlib.h> //NULL
#include "pair.h"

struct s_pair_t{
    elem fst;
    elem snd;
};

pair_t pair_new(elem x ,elem y){
    pair_t pair;
    pair=malloc(sizeof(struct s_pair_t));
    pair->fst=x;
    pair->snd=y;
    return pair;
}
elem pair_first(pair_t p){
    return p->fst;
} 
elem pair_second(pair_t p){
    return p->snd;
} 
pair_t pair_swapped(pair_t p){
    pair_t q;
    q=malloc(sizeof(struct s_pair_t));
    q->fst=p->snd;
    q->snd=p->fst;
    return q;
}
pair_t pair_destroy(pair_t p){
    free(p);
    p=NULL;
    return p;
}