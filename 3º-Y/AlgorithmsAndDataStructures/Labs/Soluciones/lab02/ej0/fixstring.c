#include <stdbool.h>
#include <assert.h>

#include "fixstring.h"

unsigned int fstring_length(fixstring s) {
    unsigned int length=0;
    while(s[length]!='\0'){
        length+=1;
    }
    return length;
}

bool fstring_eq(fixstring s1, fixstring s2) {
    bool sorted=true;
    unsigned int len_s1, len_s2;
    unsigned int j=0;
    len_s1=fstring_length(s1);
    len_s2=fstring_length(s2);
    
    if(len_s1!=len_s2){
        sorted=false;
    }else{
        while(sorted && j<len_s1){
            if(s1[j]!=s2[j]){
                sorted=false;
            }
            j+=1;
        }
    }
    return sorted;
}

bool fstring_less_eq(fixstring s1, fixstring s2){
    bool order=true;
    unsigned int j;
    bool equals=fstring_eq(s1,s2);
    bool included=true;
    unsigned int len_s1, len_s2;
    len_s1=fstring_length(s1);
    len_s2=fstring_length(s2);
    j=0;
    while(order && !equals && s1[j]!='\0'&& s2[j]!='\0'){
        if(s1[j]!=s2[j]){
            included=false;
            if(s1[j]>s2[j]){
                order=false;
            }else{
                break;
            }
        }
        j+=1;
    }

    //Sirve para comparar los casos de strings "abcd", "abcdlao"
    if(included){
        if(len_s1>len_s2){
            order=false;
        }else{
            order=true;
        }
    }
    return order;
}

