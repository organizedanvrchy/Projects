// Tic Tac Toe Game

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

// Global Variables
char board[3][3];
const char PLAYER = 'X';
const char COMPUTER = 'O';

// Functions
void reset_board();
void print_board();
int check_freespaces(); // 0 means no more spaces to move -- Game Over
void player_move();
void computer_move();
char check_winner();
void print_winner(char);

// Driver and Functions
int main() {
    char winner = ' ';
    char response;
    
    do {
        winner = ' ';
        response = ' ';

        reset_board();

        while(winner == ' ' && check_freespaces() != 0) {
            print_board();

            player_move();
            winner = check_winner();
            if (winner != ' ' || check_freespaces() == 0) {
                break;
            }

            computer_move();
            winner = check_winner();
            if (winner != ' ' || check_freespaces() == 0) {
                break;
            }
        }
    
        print_board();
        print_winner(winner);

        // Flush stdin
        while((response=getchar())!='\n' && response!=EOF) {}

        printf("\nWould you like to play again? (Y/N):");
        scanf("%c", &response);

    } while (response == 'Y');

    printf("\nThanks for playing!\n");
    system("pause");
    return 0;
}

void reset_board() {
    for(int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

void print_board() {
    printf("\n");
    printf(" %c | %c | %c ", board[0][0], board[0][1], board[0][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ", board[1][0], board[1][1], board[1][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ", board[2][0], board[2][1], board[2][2]);
    printf("\n");
}

int check_freespaces() {
    int freespaces = 9;

    for(int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] != ' ') {
                freespaces--;
            }
        }
    }
    return freespaces;
}

void player_move() {
    int x;
    int y;

    do {
        printf("\nEnter Row Number(1-3): ");
        scanf("%d", &x);
        x--;
        printf("\nEnter Column Number(1-3): ");
        scanf("%d", &y);
        y--;

        if (board[x][y] != ' ') {
            printf ("\nInvalid move.\n");
        } else {
            board[x][y] = PLAYER;
            break;
        }
    } while (board[x][y] != ' ');  

}

void computer_move(){
    // create a seed based on current time
    srand(time(0));
    int x;
    int y;

    if(check_freespaces() > 0) {
        do {
            x = rand() %3;
            y = rand() %3;
        } while(board[x][y] != ' '); 

        board[x][y] = COMPUTER;
    } else {
        print_winner(' ');
    }
}

char check_winner(){
    // check rows
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][0] == board[i][2]) {
            return board[i][0];
        }
    }

    //check columns;
    for (int i = 0; i < 3; i++) {
        if (board[0][i] == board[1][i] && board[0][i] == board[2][i]) {
            return board[0][i];
        }
    }

    //check diagonals
    for (int i = 0; i < 3; i++) {
        if (board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
            return board[0][0];
        }
    }

    for (int i = 0; i < 3; i++) {
        if (board[0][2] == board[1][1] && board[0][2] == board[2][0]) {
            return board[0][2];
        }
    }

    return ' ';
}

void print_winner(char winner){
    if (winner == PLAYER) {
        printf ("\nYou Win!\n");
    } else if (winner == COMPUTER) {
        printf ("\nYou Lose.\n");
    } else {
        printf ("\nIt's a draw.\n");
    }
}

