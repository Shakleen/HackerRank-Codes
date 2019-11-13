#include <stdio.h>

#define MAX(a, b) a > b ? a : b
#define MAX_TRACKS 21

struct ti {
	int length, taken;
} trackInfo[MAX_TRACKS];

int cdLength, tracks, finalSelection[MAX_TRACKS], max_length;
int inputCase();
void solveCase();
void printCase();
int solve(int idx, int sum);

int main() {
	while (inputCase() != EOF) {
		solveCase();
		printCase();
	}

	return 0;
}

int inputCase() {
	int i = 0;
	cdLength = EOF;

	scanf("%d", &cdLength);

	if (cdLength != EOF) {
		scanf("%d", &tracks);
		for (i = 0; i < tracks; ++i) {
			scanf("%d", &trackInfo[i].length);
			trackInfo[i].taken = finalSelection[i] = 0;
		}
	}

	return cdLength;
}

void solveCase() {
	max_length = -1;
	solve(0, 0);
}

void printCase() {
	int i = 0;

	for (i = 0; i < tracks; ++i)
		if (finalSelection[i])
			printf("%d ", trackInfo[i].length);

	printf("sum:%d\n", max_length);
}

int solve(int idx, int sum) {
	if (max_length == cdLength) return max_length;
	if (idx == tracks) {
		if (sum > max_length) {
			int i = 0;
			max_length = sum;

			for (i = 0; i < tracks; ++i) 
				finalSelection[i] = trackInfo[i].taken;
		}

		return sum;
	}

	int left = solve(idx + 1, sum), right = 0, temp = sum + trackInfo[idx].length;
	if (temp <= cdLength) {
		trackInfo[idx].taken = 1;
		right = solve(idx + 1, temp);
		trackInfo[idx].taken = 0;
	}

	return MAX(left, right);
}