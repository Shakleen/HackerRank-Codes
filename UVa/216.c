#include <stdio.h>
#include <math.h>

#define MAX_COMPUTERS 9

struct pc { int x, y, taken; } computer[MAX_COMPUTERS];
int computerNo, network;
int finalSeq[MAX_COMPUTERS], seq[MAX_COMPUTERS];
double dist[MAX_COMPUTERS][MAX_COMPUTERS], total;

int inputCase();
void solveCase();
void printCase();
double getDistance(struct pc * p1, struct pc * p2);
void solve(int idx, double sum);

int main() {
	while (inputCase()) {
		solveCase();
		printCase();
	}

	return 0;
}

int inputCase() {
	int i = 0;
	
	scanf("%d", &computerNo);
	for (i = 0; i < computerNo; ++i) {
		scanf("%d %d", &computer[i].x, &computer[i].y);
		seq[i] = -1;
		computer[i].taken = 0;
	}

	return computerNo;
}

void solveCase() {
	int i = 0, j = 0;

	for (i = 0; i < computerNo; ++i)
		for (j = i+1; j < computerNo; ++j)
			dist[i][j] = dist[j][i] = getDistance(computer + i, computer + j);

	network += 1;
	total = 9999999.0;
	solve(0, 0);
}

void printCase() {
	int i = 0, lim = computerNo - 1;

	printf("**********************************************************\n");
	printf("Network #%d\n", network);

	for (i = 0; i < lim; ++i) {
		int cur = finalSeq[i + 1], prev = finalSeq[i];
		printf(
			"Cable requirement to connect (%d,%d) to (%d,%d) is %.2lf feet.\n",
			computer[prev].x, computer[prev].y,
			computer[cur].x, computer[cur].y,
			dist[prev][cur]
		);
	}
	
	printf("Number of feet of cable required is %.2lf.\n", total);
}

void solve(int idx, double sum) {
	if (idx == computerNo) {
		if (sum < total) {
			int i = 0;

			total = sum;
			for (i = 0; i < computerNo; ++i) finalSeq[i] = seq[i];
		}

		return;
	}

	int i = 0;
	for (i = 0; i < computerNo; ++i) {
		if (computer[i].taken == 0) {
			computer[i].taken = 1;
			seq[idx] = i;
			solve(idx + 1, sum + (idx == 0 ? 0 : dist[seq[idx - 1]][i]));
			seq[idx] = -1;
			computer[i].taken = 0;
		}
	}
}

double getDistance(struct pc * p1, struct pc *p2) {
	int dx = p1->x - p2->x, dy = p1->y - p2->y;
	return sqrt(dx * dx + dy * dy) + 16.0;
}