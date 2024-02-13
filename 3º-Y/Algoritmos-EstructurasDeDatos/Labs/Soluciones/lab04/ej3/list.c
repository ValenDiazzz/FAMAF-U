#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node_t {
    list_elem elem;
    struct node_t *next;
};

list empty(){
    return NULL;
}

list addl(list l, list_elem e){
    struct node_t *p;
    p=malloc(sizeof(struct node_t));
    p->elem=e;
    p->next=l;
    return p; 
}

list destroy(list l){   
    if(l != NULL) {
        list a, b;
        a = l;
        b = a->next;
        while(a != NULL) {
            free(a);
            a = b;
            if(a != NULL) {
                b = a->next;
            }
        }
        l = a;
    }
  return l;
}

bool is_empty(list l){
    return l==NULL;
}

list_elem head(list l){
    if(is_empty(l)){
        printf("The list is empty.");
        exit(EXIT_FAILURE);
    }else{
        return l->elem;
    }
}

list tail(list l){
    if(is_empty(l)){
        printf("The list is empty.");
        exit(EXIT_FAILURE);
    }else{
        return l->next;
    }
}

list addr(list l, list_elem e){
    struct node_t *q,*p;
    q=malloc(sizeof(struct node_t));
    q->elem=e;
    q->next=NULL;
    if(l!=NULL){
        p=l;
        while(p->next != NULL){
            p=p->next;
        }
        p->next=q;
    }else{
        l=q;
    }
    return l;
}

unsigned int length(list l){
    unsigned int i=0;
    struct node_t *p;
    p=l;
    while(p!=NULL){
        p=p->next;
        i++;
    }
    return i;
}

list copy_list(list l1){
    list copy_l=empty();
    list p=l1;
    while(p!=NULL){
        addr(copy_l,p->elem);
    }
    return copy_l;
}
/*
void _exhaust_into(list src, list target) {
  list p = src;
  while(p!=NULL) {
    addr(target, p->value);
  }
}

list concat(list l1, list l2) {
  list res = empty();
  _exhaust_into(l1, res);
  _exhaust_into(l2, res);
  return res;
}
*/

list concat(list l1, list l2){
    list conc,p,q;
    conc=empty();
    p=l1;
    while(p!=NULL){
        addr(conc,p->elem);
    }
    q=l2;
    while(q!=NULL){
        addr(conc,q->elem);
    }
        
    return conc;
}

list_elem index(list l, unsigned int i){
    if(length(l)<i){
        printf("Segmentation fault.");
        exit(EXIT_FAILURE);
    }else{
        list p;
        p=l;
        for(unsigned int j=0;j<i;j++){
            p=p->next;
        }
        return p->elem;
    }
}

void take(list l, unsigned int i){
    struct node_t *p,*q;
    unsigned int j=1;
    p=l;
    while(j<i && p->next!=NULL){
        p=p->next;
        j++;
    }
    q=p->next;
    p->next=NULL;
    while(q!=NULL){
        p=q->next;
        free(q);
        q=p;
    }
}

void drop(list l, unsigned int i){
    unsigned int j=1;
    struct node_t *p,*q;
    p=l;
    while(j<i && p!=NULL){
        q=p->next;
        free(p);
        p=q;
        j++;
    }
    l=q;
}
