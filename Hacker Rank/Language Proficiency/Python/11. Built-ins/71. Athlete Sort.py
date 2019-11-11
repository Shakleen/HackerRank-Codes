N, M = map(int, input().split())
rows = []
for i in range(N): rows.append(input().split())
K = int(input())
for row in sorted(rows, key = lambda row: int(row[K])): print(' '.join(row))