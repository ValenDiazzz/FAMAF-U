#include <stdlib.h>
#include <stdio.h>

void absolute(int x, int y) {
    if (x>=0){
        y=x;
    }else{
        y=-x;
    }
}

int main(void) {
    int a=-10, res=0;
    absolute(a,res);
    printf("%d\n", res);
    return EXIT_SUCCESS;
}

/*Lo que se muestra por pantalla no coincide con el
  resultado del teórico. Por pantalla se imprime
  el número 0.
*/