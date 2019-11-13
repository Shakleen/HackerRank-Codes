#include <stdio.h>

#define MIN(a, b) a < b ? a : b
#define MAX_SIZE 21
#define MAX_BEEPERS 11
#define MAX_INT 9999999

int tests, beepers, min_len;
struct rect {
	int x, y, visited;
} worldSize, karelPos, beeperPos[MAX_BEEPERS];

void inputCase();
void solveCase();
void printCase();
int solve(int idx, int moves, struct rect * prev);
int getPathLength(struct rect * a, struct rect * b);
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
	scanf("%d %d", &worldSize.x, &worldSize.y);
	scanf("%d %d", &karelPos.x, &karelPos.y);
	scanf("%d", &beepers);

	int i = 0;
	for (i = 0; i < beepers; ++i) {
		scanf("%d %d", &beeperPos[i].x, &beeperPos[i].y);
		beeperPos[i].visited = 0;
	}
}

void solveCase() {
	min_len = solve(0, 0, &karelPos);
}

void printCase() {
	printf("The shortest path has length %d\n", min_len);
}

int solve(int idx, int moves, struct rect * prev) {
	if (idx == beepers) {
		int totalCost = moves + getPathLength(&karelPos, prev);
		return totalCost;
	}

	int i = 0, cost = MAX_INT, tempCost = 0;
	for (i = 0; i < beepers; ++i) {
		if (beeperPos[i].visited == 0) {
			beeperPos[i].visited = 1;
			tempCost = solve(
				idx + 1,
				moves + getPathLength(beeperPos + i, prev),
				beeperPos + i
			);
			beeperPos[i].visited = 0;

			cost = MIN(tempCost, cost);
		}
	}

	return cost;
}

int getPathLength(struct rect * a, struct rect * b) {
	int dx = a->x - b->x, dy = a->y - b->y;
	return abs(dx) + abs(dy);
}

int abs(int a) {
	return a < 0 ? -a : a;
}