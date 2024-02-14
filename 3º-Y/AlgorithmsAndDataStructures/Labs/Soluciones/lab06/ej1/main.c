/* First, the standard lib includes, alphabetically ordered */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

#include "abb.h" /* TAD abb */


void print_help(char *program_name) {
    /* Print the usage help of this program. */
    printf("Usage: %s <input file path>\n\n",
           program_name);
}

char *parse_filepath(int argc, char *argv[]) {
    /* Parse the filepath given by command line argument. */
    char *result = NULL;

    if (argc < 2) {
        print_help(argv[0]);
        exit(EXIT_FAILURE);
    }

    result = argv[1];

    return (result);
}

abb abb_from_file(const char *filepath) {
    FILE *file = NULL;
    abb read_tree;

    read_tree = abb_empty();
    file = fopen(filepath, "r");
    if (file == NULL) {
        fprintf(stderr, "File does not exist.\n");
        exit(EXIT_FAILURE);
    }
    unsigned int i = 0u;
    unsigned int size = 0u;
    int res = 0;
    res = fscanf(file, " %u ", &size);
    if (res != 1) {
        fprintf(stderr, "Invalid format.\n");
        exit(EXIT_FAILURE);
    }
    while (i < size) {
        abb_elem elem;
        res = fscanf(file," %d ", &(elem));
        if (res != 1) {
            fprintf(stderr, "Invalid array.\n");
            exit(EXIT_FAILURE);
        }
        read_tree = abb_add(read_tree, elem);

       ++i;
    }
    fclose(file);
    return read_tree;
}

int main(int argc, char *argv[]) {
    char *filepath = NULL;

    /* parse the filepath given in command line arguments */
    filepath = parse_filepath(argc, argv);

    /* parse the file to obtain an abb with the elements */
    abb tree = abb_from_file(filepath);

    /*dumping the tree*/
    abb_dump(tree);
    if (!abb_is_empty(tree)) {
        printf("\n");
        printf("raiz: %d\n minimo: %d\n maximo: %d\n", abb_root(tree),
                                                       abb_min(tree),
                                                       abb_max(tree));
    } else {
        printf("\nÁrbol vacío\n");
    }

    
    printf("Estan disponibles las siguientes acciones:\n");
    printf(" 1 ........ Mostrar árbol por pantalla\n"
            " 2 ........ Agregar un elemento\n"
            " 3 ........ Eliminar un elemento\n"
            " 4 ........ Chequear existencia de elemento\n"
            " 5 ........ Mostrar longitud del árbol\n"
            " 6 ........ Mostrar raiz, maximo y mínimo del árbol\n"
            " 7 ........ Salir\n"
            "Ingrese su elección: "
            );
    
    char num;
    int res=scanf("%c",&num);
    
    if (res!=1){
        printf("Opción no válida.\n");
        exit(EXIT_FAILURE);
    }
    if(num=='1'){
        abb_dump(tree);
        printf("\n");
    }else if(num=='2'){
        abb_elem elem;
        printf("Ingrese el elemento: ");
        scanf("%d",&elem);
        abb_add(tree,elem);
        printf("\nAhora el árbol es:\n");
        abb_dump(tree);
        printf("\n");
    }else if(num=='3'){
        abb_elem elem;
        printf("Ingrese el elemento: ");
        scanf("%d",&elem);
        abb_remove(tree,elem);
        printf("\nAhora el árbol es:\n");
        abb_dump(tree);
        printf("\n");
    }else if(num=='4'){
        abb_elem elem;
        printf("Ingrese el elemento: ");
        scanf("%d",&elem);
        
        printf("\n%s",abb_exists(tree,elem)?"El elemento existe.\n":"El elemento no existe.\n");
    }else if(num=='5'){
        printf("La longitud es:%u\n",abb_length(tree));
    }else if(num=='6'){
        printf("raiz: %d\n minimo: %d\n maximo: %d\n", abb_root(tree),
                                                       abb_min(tree),
                                                       abb_max(tree));
    }
    tree = abb_destroy(tree);
    return (EXIT_SUCCESS);
}
