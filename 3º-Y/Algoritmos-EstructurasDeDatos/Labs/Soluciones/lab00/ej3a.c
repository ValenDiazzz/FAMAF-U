#include <stdlib.h>  /* exit() y EXIT_FAILURE */
#include <stdio.h>   /* printf(), scanf()     */
#include <stdbool.h> /* Tipo bool             */

#include <assert.h>  /* assert() */

#define CELL_MAX (4 * 4 - 1)
#define N 4
void print_sep(int length) {
    printf("\t ");
    for (int i=0; i < length;i++) printf("................");
    printf("\n");

}

void print_board(char board[N][N])
{
    int cell = 0;

    print_sep(N);
    for (int row = 0; row < N; ++row) {
        for (int column = 0; column < N; ++column) {
            printf("\t | %d: %c ", cell, board[row][column]);
            ++cell;
        }
        printf("\t | \n");
        print_sep(N);
    }
}

char get_winner(char board[N][N])
{
    char winner = '-';
	unsigned int i,j,k;
	bool winner_found=false;
	bool flag;
	//filas
	i=0;
	while(i<N && !winner_found){
		flag=true;
		for(k=0;k<N-1;k++){
			flag= flag && (board[i][k]==board[i][k+1]) && board[i][k]!='-';
		}
		if(flag){
			winner=board[i][0];
			winner_found=true;
		}
		i+=1;			
	}
	//columnas
	j=0;
	while(j<N && !winner_found){
		flag=true;
		for(k=0;k<N-1;k++){
			flag= flag && (board[k][j]==board[k+1][j]) && board[k][j]!='-';
		}
		if(flag){
			winner=board[0][j];
			winner_found=true;
		}
		j+=1;		
	}
	//diagonales
	if(!winner_found){
		flag=true;
		for(k=0;k<N-1;k++){
			flag= flag && (board[k][k]==board[k+1][k+1]) && board[k][k]!='-';
		}
		if(flag){
			winner=board[0][0];
			winner_found=true;
		}			
	}

	if(!winner_found){
		flag=true;
		for(k=0;k<N-1;k++){
			flag= flag && (board[k][N-1-k]==board[k+1][N-2-k]) && board[k][N-1-k]!='-';
		}
		if(flag){
			winner=board[0][N-1];
			winner_found=true;
		}			
	}
	if(!winner_found){
		winner='-';
	}
	return winner;
}

bool has_free_cell(char board[N][N])
{
	bool free_cell=false;
	unsigned int i,j;
		for(i=0; i<N;i++){
			for(j=0; j<N;j++){
				if (board[i][j]=='-'){
					free_cell=true;
					break;
				}
			}
			if (free_cell==true){
				break;
			}
		}
		return free_cell;
}


int main(void)
{
    printf("TicTacToe [InCoMpLeTo :'(]\n");

    char board[N][N] = {
        { '-', '-', '-','-' },
        { '-', '-', '-','-' },
        { '-', '-', '-','-' },
        { '-', '-', '-','-' }
    };

    char turn = 'X';
    char winner = '-';
    int cell = 0;
    while (winner == '-' && has_free_cell(board)) {
        print_board(board);
        printf("\nTurno %c - Elija posición (número del 0 al %d): ", turn,
               CELL_MAX);
        int scanf_result = scanf("%d", &cell);
        if (scanf_result <= 0) {
            printf("Error al leer un número desde teclado\n");
            exit(EXIT_FAILURE);
        }
        if (cell >= 0 && cell <= CELL_MAX) {
            int row = cell / N;
            int colum = cell % N;
            if (board[row][colum] == '-') {
                board[row][colum] = turn;
                turn = turn == 'X' ? 'O' : 'X';
                winner = get_winner(board);
            } else {
                printf("\nCelda ocupada!\n");
            }
        } else {
            printf("\nCelda inválida!\n");
        }
    }
    print_board(board);
    if (winner == '-') {
        printf("Empate!\n");
    } else {
        printf("Ganó %c\n", winner);
    }
    return 0;
}