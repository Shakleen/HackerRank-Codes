#include <stdio.h>

#define MAX_OBJECTS 1001
#define MAX_PEOPLE 101
#define MAX_WEIGHT 31
#define MAX(a, b) a > b ? a : b

int tests, objects, people, person[MAX_PEOPLE], total_value;
int dp[MAX_WEIGHT];


void init();
void inputCase();
void solveCase();
void printCase();

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int tc = 0;
    
    scanf("%d", &tests);

    for (tc = 1; tc <= tests; ++tc) {
        init();
        inputCase();
        solveCase();
        printCase();
    }

    return 0;
}

void init() {
    int i = 0;
    for (i = 0; i < 31; ++i) dp[i] = 0;
    total_value = 0;
}

void inputCase() {
    int i = 0, j = 0, price = 0, weight = 0;

    scanf("%d", &objects);
    for (i = 0; i < objects; ++i) {
        scanf("%d %d", &price, &weight);
        
        for (j = MAX_WEIGHT-1; j >= weight; --j)
            dp[j] = MAX(dp[j], dp[j - weight] + price);
    }

    scanf("%d", &people);
    for (i = 0; i < people; ++i) 
        scanf("%d", &person[i]);
}

void solveCase() {
    int i = 0;
    for (i = 0; i < people; ++i)
        total_value += dp[person[i]];
}

void printCase() {
    printf("%d\n", total_value);
}