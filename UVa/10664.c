#include <stdio.h>

#define MIN(a, b) a < b ? a : b
#define MAX_SUIT_CASES 21
#define MAX_INT 9999999
#define MAX_SUM 201

int tests, suitCases[MAX_SUIT_CASES], minDiff, suitCaseNo, total = 0;
int dp[MAX_SUIT_CASES][MAX_SUM];
void inputCase();
void solveCase();
void printCase();
int abs(int a);

int main() {
	int tc = 0;

	scanf("%d", &tests);
	for (tc = 1; tc <= tests; ++tc) {
		inputCase();
		solveCase();
		printCase();
	}

	return 0;
}

void inputCase() {
	int a = 0;
	suitCaseNo = 0;
	total = 0;

	while (scanf("%d", &a) != EOF) {
		suitCases[suitCaseNo++] = a;
		total += a;
		if (getchar() == '\n') break;
	}
}

void solveCase() {
	int i = 0, j = 0;

	for (i = 0; i <= suitCaseNo; ++i)
		for (j = 0; j <= total; ++j)
			dp[i][j] = -1;

	minDiff = solve(0, 0);
}

void printCase() {
	printf(minDiff == 0 ? "YES" : "NO");
	printf("\n");
}

int solve(int idx, int sum) {
	if (dp[idx][sum] != -1) return dp[idx][sum];

	if (idx == suitCaseNo) {
		int diff = abs(2 * sum - total);
		return dp[idx][sum] = diff;
	}

	int left = solve(idx + 1, sum);
	int right = solve(idx + 1, sum + suitCases[idx]);
	return dp[idx][sum] = MIN(left, right);
}

int abs(int a) {
	return a < 0 ? -a : a;
}