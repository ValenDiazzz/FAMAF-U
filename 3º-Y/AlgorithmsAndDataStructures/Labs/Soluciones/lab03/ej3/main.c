#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#define MAX_SIZE 1000

static void dump(char a[], unsigned int length) {
    printf("\"");
    for (unsigned int j=0u; j < length; j++) {
        printf("%c", a[j]);
    }
    printf("\"");
    printf("\n\n");
}

unsigned int data_from_file(
    const char *path,
    unsigned int indexes[],
    char letters[],
    unsigned int max_size){
    
    unsigned int length=0;
    FILE *f;
    f=fopen(path, "r");

    while(length<max_size && !feof(f)){
        fscanf(f,"%u -> *%c* \n", &indexes[length], &letters[length]);
        length++;
    }
    fclose(f);

    return length;

}

char *parse_filepath(int argc, char *argv[]) {
    /* Parse the filepath given by command line argument. */
    char *result = NULL;
    // Program takes exactly two arguments
    // (the program's name itself and the input-filepath)
    bool valid_args_count = (argc == 2);

    if (!valid_args_count) {
        exit(EXIT_FAILURE);
    }

    result = argv[1];

    return result;
}

void letters_sort(char a[],unsigned int index[], unsigned int length){
    char letra;
    unsigned int i,idx;

    for(unsigned int j=0;j<length;j++){
        i=j;
                
        //No quiero que mi idx sea igual que j, sino me pierdo el swap
        while(index[i]!=j){
            i++;
        }
        idx=index[i];
        letra=a[i];
        index[i]=index[j];
        a[i]=a[j];
        index[j]=idx;
        a[j]=letra;
    }    
}

int main(int argc, char *argv[]) {
    unsigned int indexes[MAX_SIZE];
    char letters[MAX_SIZE];
    char *file;
    unsigned int length=0; 

    file= parse_filepath(argc, argv);
    length=data_from_file(file,indexes,letters,MAX_SIZE);
    
    letters_sort(letters,indexes,length);
    dump(letters, length);
    return EXIT_SUCCESS;
}

