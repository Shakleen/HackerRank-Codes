n = int(input())
heights = list(map(int, input().split()))
print(heights.count(max(heights)))