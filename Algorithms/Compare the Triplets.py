aliceScores = list(map(int, input().split()))
bobScores = list(map(int, input().split()))

alicePoints = bobPoints = 0
for (a, b) in zip(aliceScores, bobScores):
    alicePoints += a > b
    bobPoints += a < b

print('{} {}'.format(alicePoints, bobPoints))