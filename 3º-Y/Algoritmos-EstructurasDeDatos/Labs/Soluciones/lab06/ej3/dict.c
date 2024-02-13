#include <assert.h>
#include <stdlib.h>
#include "dict.h"
#include "key_value.h"

struct _node_t {
    dict_t left;
    dict_t right;
    key_t key;
    value_t value;
};

//This function takes a subtree root and checks if the elements below are greater.
static bool left_dict(dict_t dict, key_t word){
    static bool res=true;
    if (dict!=NULL){
        res = (key_less(dict->key, word) || !key_eq(dict->key, word))
                                       && left_dict(dict->left, word)
                                       && left_dict(dict->right, word);
    }
    return res;
}
//This function takes a dict root and checks if the elements below are smaller.
static bool right_dict(dict_t dict, key_t word){
    static bool res=true;
    if (dict!=NULL){
        res = (key_less(word, dict->key) || !key_eq(word,dict->key))
                                       && right_dict(dict->left, word)
                                       && right_dict(dict->right, word);
    }
    return res;
}

static bool invrep(dict_t dict) {
    static bool res=true;
    if (dict!=NULL){
        dict_t lft, rgt;
        key_t word;
        lft=dict->left;
        rgt=dict->right;
        word=dict->key;

        res= left_dict(lft,word) && right_dict(rgt,word);
        res= res && invrep(lft) && invrep(rgt);;
    }
    return res;
}

dict_t dict_empty(void) {
    dict_t dict = NULL;
    return dict;
}

dict_t dict_add(dict_t dict, key_t word, value_t def) {
    assert(invrep(dict));
    if(dict == NULL) {
        dict = malloc(sizeof(struct _node_t));
        dict->key=word;
        dict->value=def;
        dict->left = NULL;
        dict->right = NULL;
    
    }else if(key_less(word, dict->key)) {
        dict->left = dict_add(dict->left, word, def);
    
    }else if(key_less(dict->key, word)){
        dict->right = dict_add(dict->right, word,def);
    
    }else{
        value_t tmp;
        tmp = dict->value;
        dict->value=def;
        key_destroy(tmp);
    }

    assert(invrep(dict));
    //assert(dict_exists(dict, word));
    return dict;
}

value_t dict_search(dict_t dict, key_t word) {
    value_t def=NULL;
    while(dict!=NULL && !key_eq(word, dict->key)){
        if(key_less(word, dict->key)){
            dict=dict->left;
        }else{
            dict=dict->right;
        }
    }
    if(dict!=NULL){
        def=dict->value;
    }
    return def;
}

bool dict_exists(dict_t dict, key_t word) {
    bool exists=false;
    while(!exists && dict!=NULL){
        if(key_less(word, dict->key)){
            dict=dict->left;
        }else if(!key_eq(word, dict->key)){
            dict=dict->right;
        }else{
            exists=true;
        }
    }
    return exists;
}
unsigned int dict_length(dict_t dict) {
    unsigned int len=0;
    if(dict!=NULL){
        len+=1;
        len+= dict_length(dict->left)+dict_length(dict->right);
    }
    return len;
}

key_t dict_max(dict_t dict) { //Returns the greater word of the dictionary.
    assert(invrep(dict));
    key_t max_key;
    struct _node_t *d;
    d=dict;
    while(d->right!=NULL){
        d=d->right;
    }
    max_key=d->key;
    return max_key;
}

dict_t del_max(dict_t dict){ //destroy the node of the greater word.
    assert(invrep(dict));
    dict_t left;
    if (dict->right==NULL){
        left = dict->left;
        free(dict);
        dict = left;
    }else{
        dict->right = del_max(dict->right);
    }
    return dict;
}

dict_t dict_remove(dict_t dict, key_t word) { //lm
    assert(invrep(dict));
    if (dict!=NULL){
        key_t key=dict->key;
        if (key_less(key,word)){
            dict->right=dict_remove(dict->right, word);
        }else if (key_less(word,key)){
            dict->left=dict_remove(dict->left, word);
        //replace removed node with its right subdict    
        }else if (key_eq(word, key) && dict->left==NULL){
            dict_t right=dict->right;
            free(dict);
            dict=right;
        }else{  //replace the removed node with the max key of left subdict
            dict->key=dict_max(dict->left);
            del_max(dict->left);
        }
    }
    assert(invrep(dict) && !dict_exists(dict,word));
    return dict;
}

dict_t dict_remove_all(dict_t dict) {
    assert(invrep(dict));
    if(dict!=NULL){
       dict->left=dict_remove_all(dict->left);
       dict->right=dict_remove_all(dict->right);
       dict->key=key_destroy(dict->key);
       dict->value=value_destroy(dict->value);
       free(dict);
       dict=NULL;
    }
    assert(invrep(dict) && dict_length(dict)==0);
    return dict;
}

void dict_dump(dict_t dict, FILE *file) {
    assert(invrep(dict) && file!=NULL);
    if (dict != NULL) {
        // Dump in-order
        dict_dump(dict->left, file);
        key_dump(dict->key, file);
        fprintf(file, ": ");
        key_dump(dict->value, file);
        fprintf(file, "\n");
        dict_dump(dict->right, file);
    }
}

dict_t dict_destroy(dict_t dict) {
    assert(invrep(dict));
    if(dict!=NULL){

        dict->left=dict_destroy(dict->left);
        dict->right=dict_destroy(dict->right);
        dict->key = key_destroy(dict->key);
        dict->value = value_destroy(dict->value);
        free(dict);
        dict=NULL;
    }
    assert(dict==NULL);
    return dict;
}
