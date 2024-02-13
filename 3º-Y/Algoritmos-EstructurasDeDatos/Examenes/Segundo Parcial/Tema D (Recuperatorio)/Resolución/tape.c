#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include "tape.h"

struct _s_node {
    tape_elem elem;
    struct _s_node *next;
};

typedef struct _s_node * node_t;

struct _s_tape {
    unsigned int size;
    node_t cursor;  // Puntero al elemento actual
    node_t start;   // Puntero al primer nodo de la cinta
};

static bool invrep(tape_t tape) {//(void){
    bool res;
    if(tape==NULL){
        res=false;
    }else{
        unsigned int len=0;
        struct _s_node *curr;
        curr=tape->start;
        while(curr!=NULL){
            curr=curr->next;
            len++;
        }
        res= len==tape->size;
    }

    return res;//return true
}

static node_t create_node(tape_elem e) {
    struct _s_node *node=malloc(sizeof(struct _s_node));
    node->elem=e;
    node->next=NULL;
    return node;
}

static node_t destroy_node(node_t node) {
    if(node!=NULL){
        free(node);
        node=NULL;
    }

    return node;
}

tape_t tape_create(void) {
    tape_t tape=NULL;
    tape=malloc(sizeof(struct _s_tape));
    tape->size=0;
    tape->cursor=NULL;
    tape->start=NULL;
    assert(invrep(tape) && tape_is_empty(tape) && tape_at_start(tape));
    return tape;
}

tape_t tape_rewind(tape_t tape) {
    assert(invrep(tape));
    tape->cursor=tape->start;
    assert(invrep(tape) && tape_at_start(tape));
    return tape;
}


bool tape_at_start(tape_t tape) {
    assert(invrep(tape));
    return tape->cursor==tape->start;
}

bool tape_at_stop(tape_t tape) {
    assert(invrep(tape));
    return tape->cursor==NULL;
}

bool tape_is_empty(tape_t tape) {
    assert(invrep(tape));
    return tape->size==0;
}

unsigned int tape_length(tape_t tape) {
    assert(invrep(tape));
    return tape->size;
}

tape_t tape_step(tape_t tape) {
    assert(invrep(tape));
    if(tape->cursor!=NULL){
        tape->cursor = tape->cursor->next;
    }
    return tape;
}

tape_t tape_insertl(tape_t tape, tape_elem e) {
    assert(invrep(tape));
    struct _s_node *new_node=create_node(e);

    if(!tape_is_empty(tape) && !tape_at_start(tape)){
        struct _s_node *pre,*pos;
        pos=tape->start;
        
        while(pos!=tape->cursor){
            pre=pos;
            pos=pos->next;
        }
        pre->next=new_node;
        new_node->next=pos;
    }else{ //cursor not at start or tape is empty.
        if(tape_is_empty(tape)){
            tape->start=new_node;
        }else{
            struct _s_node *aux;
            aux=tape->start;
            tape->start=new_node;
            new_node->next=aux;
        } 
    }
    tape->cursor=new_node;
    tape->size++;
    assert(invrep(tape)&& !tape_is_empty(tape) && !tape_at_stop(tape) && e == tape_read(tape));
    return tape;
}

tape_t tape_insertr(tape_t tape, tape_elem e) {
    assert(invrep(tape) && (!tape_at_stop(tape) || tape_is_empty(tape)));
    node_t new_node=create_node(e);
    if (tape->start!= NULL) {
        new_node->next = tape->cursor->next;
        tape->cursor->next = new_node;
        tape->cursor = new_node;
    } else {
        tape->start = new_node;
        tape->cursor = new_node;
    }
    tape->size++;
    assert(invrep(tape) && !tape_is_empty(tape) && !tape_at_stop(tape) && e == tape_read(tape));
    return tape;
}

tape_t tape_erase(tape_t tape) {
    assert(invrep(tape)&& !tape_is_empty(tape) && !tape_at_stop(tape)); //=> cursor!=NULL
    struct _s_node *pre,*pos;
    struct _s_node *killme=tape->cursor;
    pre=NULL;
    pos=tape->start;
    while(pos!=tape->cursor){
        pre=pos;
        pos=pos->next;
    }
    //pos is in cursor and pre is previous.
    if(pre==NULL){ //when cursor is at start
        tape->start=pos->next;
    }else{
        pre->next=pos->next;
    }
    tape->cursor=tape->cursor->next;
    killme=destroy_node(killme);
    tape->size--;

    assert(invrep(tape));
    return tape;
}

tape_elem tape_read(tape_t tape) {
    assert(invrep(tape) && !tape_is_empty(tape) && !tape_at_stop(tape));
    return tape->cursor->elem;
}

void tape_dump(tape_t tape) {
    assert(invrep(tape));
    node_t node=tape->start;
    printf("#");
    while (node != NULL) {
        if (node != tape->cursor) {
            printf("-%c-", node->elem);
        } else {
            printf("-[%c]-", node->elem);
        }
        node = node->next;
    }
    if (tape->cursor==NULL) {
        printf("-[]-");
    }
    printf("#\n");
}

tape_t tape_copy(tape_t tape){
    assert(invrep(tape));
    struct _s_node *p;
    tape_t copy;
    tape_elem e;
    
    copy=tape_create();
    unsigned int len=tape_length(tape);
    p=tape->start;
    for(unsigned int i=0;i<len;i++){
        e=p->elem;
        copy=tape_insertr(copy, e);
        p=p->next;
    }
    copy->cursor=copy->start;
    assert(invrep(copy) && copy != tape && tape_at_start(copy) && tape_length(tape) == tape_length(copy));
    return copy;
}

tape_t tape_destroy(tape_t tape) {
    assert(invrep(tape));
    struct _s_node *killme,*p;
    p=tape->start;
    while(p!=NULL){
        killme=p;
        p=p->next;
        killme=destroy_node(killme);
    }
    tape->start=NULL;
    tape->cursor=NULL;
    free(tape);
    tape=NULL;
    assert(tape==NULL);
    return tape;
}


