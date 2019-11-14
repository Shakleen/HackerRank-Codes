#include <stdio.h>

#define MAX_NUMBER 1121
#define TOTAL_PRIMES 187
#define MAX_K 15

int number, k, ways, prime[TOTAL_PRIMES];
int dp[MAX_NUMBER][MAX_K], isPrime[MAX_NUMBER];

void generatePrimes();
void preprocess();
int inputCase();
void printCase();

int main() {
	generatePrimes();
	preprocess();
	while (inputCase()) printCase();
	return 0;
}

void generatePrimes() {
	int i = 0, j = 0, count = 0;
	prime[0] = 2;

	for (i = 3; i < MAX_NUMBER; i += 2) 
		if (isPrime[i] == 0) 
			for (j = i * i, prime[++count] = i; j < MAX_NUMBER; j += i << 1)
				isPrime[j] = 1;
}

int inputCase() {
	scanf("%d %d", &number, &k);
	return number != 0 && k != 0;
}

void printCase() {
	printf("%d\n", dp[number][k]);
}

void preprocess() {
	int i = 0, j = 0, k = 0;

	dp[0][0] = 1;
	for (i = 0; i < TOTAL_PRIMES; ++i)
		for (j = MAX_NUMBER - 1; j >= prime[i]; --j)
			for (k = MAX_K - 1; k > 0; --k)
				dp[j][k] += dp[j - prime[i]][k - 1];
}