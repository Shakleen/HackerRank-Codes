tests = int(input())

for t in range(tests):
    budget, cost, trade = map(
        int, input().split()
    )

    count = budget // cost
    canTrade = count

    while canTrade >= trade:
        bought = canTrade // trade
        left = canTrade % trade
        canTrade = bought + left
        count += bought

    print(count)