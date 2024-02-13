#include <stdlib.h>
#include <stdio.h>

void absolute(int x, int *y) {
    if (x>=0){
        *y=x;
    }else{
        *y=-x;
    }
}

int main(void) {
    int a=0, res=0;  // No modificar esta declaración
    int *p=NULL;
    p=&res;
    absolute(a,p);
    printf("%d\n", res);
    return EXIT_SUCCESS;
}

//El parámetro *y de absolute es de tipo in.
//C solo tiene parametros de tipo in.