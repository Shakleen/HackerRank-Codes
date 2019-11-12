#include <stdio.h>

#define SIZEM 101
#define SIZEDP 50001

int M;
int coin_values[SIZEM];
int min_value;
int total;
int dp[SIZEM][SIZEDP];

void inputCase();
void solveCase();
void printCase();
int solve(int idx, int sum1);
int getDiff(int no1, int no2);
int getMin(int no1, int no2);

int main() {
	int tests = 0, tc = 0;
	scanf("%d", &tests);

	for (tc = 1; tc <= tests; ++tc) {
		inputCase();
		solveCase();
		printCase();
	}

	return 0;
}

void inputCase() {
	int i = 0;
	total = 0;

	scanf("%d", &M);

	for (i = 1; i <= M; ++i) {
		scanf("%d", &coin_values[i]);
		total += coin_values[i];
	}

	min_value = total;
}

void solveCase() {
	int i = 0, j = 0;

	for (i = 0; i <= M; ++i) {
		for (j = 0; j <= total; ++j) {
			dp[i][j] = -1;
		}
	}

	min_value = solve(0, 0);
}

void printCase() {
	printf("%d\n", min_value);
}

int solve(int idx, int sum1) {
	if (-1 != dp[idx][sum1]) return dp[idx][sum1];

	if (idx == M) {
		dp[idx][total-sum1] = dp[idx][sum1] = getDiff(sum1, total - sum1);
		return dp[idx][sum1];
	}

	int left = solve(idx + 1, sum1);
	int right = solve(idx + 1, sum1 + coin_values[idx]);
	return dp[idx][sum1] = getMin(left, right);
}

int getMin(int no1, int no2) {
	return no1 < no2 ? no1 : no2;
}

int getDiff(int no1, int no2) {
	return no1 < no2 ? no2 - no1 : no1 - no2;
}