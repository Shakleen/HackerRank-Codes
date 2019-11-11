def takeInput(): 
    a, b = map(int, input().split())
    return (a, b)

def isInBound(x, y): 
    return (1 <= x <= n) and (1 <= y <= n)

def isNotBlocked(x, y):
    return block_pos.get((x,y), 1)

directions = [(1,1), (1,0), (1,-1), (-1,1), (-1,0), (-1,-1), (0,1), (0,-1)]
n, k = takeInput()
rq, cq = takeInput()
block_pos = {takeInput(): 0 for _ in range(k)}
count = 0

for (r, c) in directions:
    rt, ct = rq, cq

    while True:
        rt, ct = rt + r, ct + c

        if isInBound(rt, ct) and isNotBlocked(rt, ct):
            count += 1
        else:
            break

print(count)
