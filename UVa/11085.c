#include <stdio.h>

#define MAX 8
#define MAX_INT 2147483647
#define TYPES 92

int testCase, queen_pos[MAX], min_moves, types;
int boardConfig[TYPES][MAX];

int inputCase();
void solveCase();
void printCase();
void solve(int idx, int moves);
int noAttackingPair();
void preprocess();

int main() {
    preprocess(0, 0);

    while (inputCase() != EOF) {
        solveCase();
        printCase();
    }

    return 0;
}

int inputCase() {
    int res = -1, i = 0;

    for (i = 0; i < MAX; ++i) {
        scanf("%d", &res);

        if (res == EOF) 
            return EOF;
        else 
            queen_pos[i] = res;
    }
    
    return res;
}

void solveCase() {
    min_moves = MAX_INT;
    
    int i = 0, j = 0, moves = 0;
    for (i = 0; i < TYPES; ++i) {
        moves = 0;

        for (j = 0; j < MAX; ++j) {
            moves += queen_pos[j] != boardConfig[i][j];
        }

        min_moves = min_moves > moves ? moves : min_moves;
    }
}

void printCase() {
    printf("Case %d: %d\n", ++testCase, min_moves);
}

int noAttackingPair() {
    int i, j;

    for (i = 0; i < MAX; ++i) {
        for (j = i + 1; j < MAX; ++j) {
            if (queen_pos[i] == queen_pos[j]) 
                return 0;
            else if ((queen_pos[i] - i) == (queen_pos[j] - j)) 
                return 0;
            else if ((queen_pos[i] - (9 - i)) == (queen_pos[j] - (9 - j))) 
                return 0;
        }
    }

    return 1;
}

void preprocess(int idx, int moves) {
    if (idx == MAX) {
        if (noAttackingPair()) {
            int i = 0;
            for (i = 0; i < MAX; ++i) boardConfig[types][i] = queen_pos[i];
            types += 1;
        }
        return;
    }

    int i = 0;
    for (i = 1; i <= MAX; ++i) {
        int tempx = queen_pos[idx];
        queen_pos[idx] = i;
        preprocess(
            idx + 1, 
            moves + (i == tempx ? 0 : 1)
        );
        queen_pos[idx] = tempx;
    }
}