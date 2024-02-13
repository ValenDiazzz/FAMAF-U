#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include "list.h"

struct _node_t {
  unsigned int key;
  list_value value;
  struct _node_t *next;
};

typedef struct _node_t * node_t;

struct _list_t {
  unsigned int len;
  node_t elems;
};

static bool invrep(list_t list) {
    bool res;
    if(list==NULL){
        res=false;
    }else{
        res=true;
        unsigned int i=1;

        struct _node_t *pre,*pos;
        pre=list->elems;

        while(res && pre!=NULL){ //Checks fundamental property.
            pos=pre->next;
            if(pos!=NULL){
                res=pre->key < pos->key;
                i++;
            }
            pre=pos;
        }

        if (res && list->len!=0 && list->len!=i){ //checks if its len is correct.
            res=false;
        }
    }
    return res;
}

static struct _node_t * create_node(unsigned int key, list_value value) {
  struct _node_t *new_node;
  new_node=malloc(sizeof(struct _node_t));
  new_node->key=key;
  new_node->value=value;
  new_node->next=NULL;
  return new_node;
}

static struct _node_t * destroy_node(struct _node_t *node) {
  free(node);
  node=NULL;
  return node;
}

list_t list_empty(void) {
  struct _list_t *l=malloc(sizeof(struct _list_t));
  l->len=0;
  l->elems=NULL;
  assert(invrep(l));
  assert(l->len==0);
  return l;
}

list_t list_add(list_t list, unsigned int key, list_value value) {
    assert(invrep(list));
    struct _node_t *new_node=create_node(key,value);

    if(list->len==0){
        list->elems=new_node;
    }else{
        struct _node_t *pre,*pos;

        pre=NULL;
        pos=list->elems;
        while(pos!=NULL && key > pos->key ){
            pre=pos;
            pos=pos->next;
        }
        if(pos!=NULL){  //pos didnt reach the end of the list and pos->key greater than key
            if(key == pos->key){    //key exists
                pos->value=value;
                new_node=destroy_node(new_node);
            }else{      //key doesnt exists
                if(pre!=NULL){  //pos not in first element
                    pre->next=new_node;
                    new_node->next=pos;
                }else{ //pos in first element
                    new_node->next=pos;
                    list->elems=new_node;
                }
            }
        }else if(pre!=NULL){ //pos reached the end of list and list not empty
            pre->next=new_node;
        }
    }

    list->len++; //update list length
    return list;
}

unsigned int list_length(list_t list) {
  assert(invrep(list));
  return list->len;
}

bool list_is_empty(list_t list) {
  assert(invrep(list));
  return list->len==0;
}

bool list_exists(list_t list, unsigned int key) {
  assert(invrep(list));

  node_t elem = list->elems;
  while (elem != NULL && elem->key < key) {
    elem = elem->next;
  }
  return elem != NULL && elem->key == key;
}


char list_search(list_t list, unsigned int key) {
  assert(invrep(list));
  assert(list_exists(list,key));

  struct _node_t *p;
  p=list->elems;
  while(p->key != key){//finds the node containing the key.
    p=p->next;
  }

  return p->value;

}

list_t list_remove(list_t list, unsigned int key) {
    assert(invrep(list));   
    struct _node_t *pre,*pos;
    pre=NULL;
    pos=list->elems;
    while(pos!=NULL && key != pos->key){
        pre=pos;
        pos=pos->next;
    }
    if(pos!=NULL){
        if(pre==NULL){ //key is first elem and list is not empty.
            pos=destroy_node(pos);
            list->len--;
        }else{
            pre->next=pos->next;
            pos=destroy_node(pos);
            list->len--;
        }
    }
    return list;
}

list_t list_remove_all(list_t list) {
  assert(invrep(list));
    struct _node_t *pre,*pos;
    pre=list->elems;
    while(pre!=NULL){
      pos=pre->next;
      pre=destroy_node(pre);
      pre=pos;
    }
    list->len=0;
    return list;
}


list_value* list_to_array(list_t list) {
    assert(invrep(list));
    
    list_value *array=NULL;
    unsigned int size=list_length(list);
    array=malloc(sizeof(list_value)*(size));
    struct _node_t *p;

    unsigned int i=0;
    p=list->elems;
    while(i<size){
        array[i]=p->value;
        p=p->next;
        i++;
    }   
    return array;
}

list_t list_destroy(list_t list) {
  assert(invrep(list));
  struct _node_t *pre,*pos;
  pre=list->elems;
  while(pre!=NULL){
    pos=pre->next;
    pre=destroy_node(pre);
    pre=pos;
  }
  free(list);
  list=NULL;
  return list;
}
