#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include "abb.h"

struct _s_abb {
    abb_elem elem;
    struct _s_abb *left;
    struct _s_abb *right;
};


static bool elem_eq(abb_elem a, abb_elem b) {
    return a == b;
}

static bool elem_less(abb_elem a, abb_elem b) {
    return a < b;
}

//This function takes a subtree root and checks if the elements below are greater.
static bool left_subtree(abb tree, abb_elem e){
    static bool res=true;
    if (tree!=NULL){
        res = (elem_less(tree->elem, e) || !elem_eq(tree->elem, e))
                                       && left_subtree(tree->left, e)
                                       && left_subtree(tree->right, e);
    }
    return res;
}
//This function takes a subtree root and checks if the elements below are smaller.
static bool right_subtree(abb tree, abb_elem e){
    static bool res=true;
    if (tree!=NULL){
        res = (elem_less(e, tree->elem) || !elem_eq(e,tree->elem))
                                       && right_subtree(tree->left, e)
                                       && right_subtree(tree->right, e);
    }
    return res;
}

static bool invrep(abb tree) {
    static bool res=true;
    if (tree!=NULL){
        abb lft, rgt;
        abb_elem e;
        lft=tree->left;
        rgt=tree->right;
        e=tree->elem;

        res= left_subtree(lft,e) && right_subtree(rgt,e);
        res= res && invrep(lft) && invrep(rgt);;
    }
    return res;
}

abb abb_empty(void) {
    abb tree;
    tree=NULL;
    assert(invrep(tree) && abb_is_empty(tree));
    return tree;
}

abb abb_add(abb tree, abb_elem e) {
    assert(invrep(tree));

    if(tree==NULL){
        tree = malloc(sizeof(struct _s_abb));
        tree->elem = e;
        tree->left = NULL;
        tree->right = NULL;
    }else{
        abb_elem root=tree->elem;
        if(e>root){
            tree->right=abb_add(tree->right,e);
        }else if(e<root){
            tree->left=abb_add(tree->left,e);
        }else{
            printf("Reapeted elements are not allowed.\n");
            exit(EXIT_FAILURE);
        }
    }
    assert(invrep(tree) && abb_exists(tree, e));
    return tree;
}

bool abb_is_empty(abb tree) {
    bool is_empty=false;
    assert(invrep(tree));
    is_empty= tree==NULL ? true:false;
    return is_empty;
}

bool abb_exists(abb tree, abb_elem e) {
    bool exists=false;
    assert(invrep(tree));
    if(tree==NULL){
        exists=false;
    }else if(e==tree->elem){
        exists=true;
    }else if(e>tree->elem){
        exists=abb_exists(tree->right,e);
    }else{
        exists=abb_exists(tree->left,e);
    }

    return exists;
}

unsigned int abb_length(abb tree) {
    unsigned int length=0;
    assert(invrep(tree));
    if(tree!=NULL){
        length+=1;
        length+= abb_length(tree->left) + abb_length(tree->right);
    }
    assert(invrep(tree) && (abb_is_empty(tree) || length > 0));
    return length;
}

abb del_max(abb tree){ //destroy the node of the max elem
    abb left;
    if (abb_is_empty(tree->right)){
        left = tree->left;
        free(tree);
        tree = left;
    }else{
    tree->right = del_max(tree->right);
    }
    return tree;
}

abb abb_remove(abb tree, abb_elem e) {
    assert(invrep(tree));
    if (!abb_is_empty(tree)){
        abb_elem root=tree->elem;
        if (root < e){
            tree->right=abb_remove(tree->right, e);
        }else if (root > e){
            tree->left=abb_remove(tree->left, e);
        //replace removed node with its right subtree    
        }else if ((e == root) && abb_is_empty(tree->left)){
            abb right=tree->right;
            free(tree);
            tree=right;

        }else{  //replace de removed node with the max elem of left subtree
            tree->elem=abb_max(tree->left);
            del_max(tree->left);
        }
    }
   
    assert(invrep(tree) && !abb_exists(tree, e));
    return tree;
}


abb_elem abb_root(abb tree) {
    abb_elem root;
    assert(invrep(tree) && !abb_is_empty(tree));
    root=tree->elem;
    assert(abb_exists(tree, root));
    return root;
}

abb_elem abb_max(abb tree) {
    abb_elem max_e;
    assert(invrep(tree) && !abb_is_empty(tree));
    
    struct _s_abb *p;
    p=tree;
    while(p->right!=NULL){
        p=p->right;
    }
    max_e=p->elem;
    assert(invrep(tree) && abb_exists(tree, max_e));
    return max_e;
}

abb_elem abb_min(abb tree) {
    abb_elem min_e;
    assert(invrep(tree) && !abb_is_empty(tree));
    struct _s_abb *p;
    p=tree;
    while(p->left!=NULL){
        p=p->left;
    }
    min_e=p->elem;
    assert(invrep(tree) && abb_exists(tree, min_e));
    return min_e;
}

void abb_dump(abb tree) {
    assert(invrep(tree));
    if (tree != NULL) {
        abb_dump(tree->left);
        printf("%d ", tree->elem);
        abb_dump(tree->right);
    }
}

abb abb_destroy(abb tree) {
    assert(invrep(tree));
    if(tree!=NULL){

        tree->left=abb_destroy(tree->left);
        tree->right=abb_destroy(tree->right);

        free(tree);
        tree=NULL;
    }
    assert(tree == NULL);
    return tree;
}

