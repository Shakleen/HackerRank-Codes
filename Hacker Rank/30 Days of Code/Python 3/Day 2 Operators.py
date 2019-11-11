mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

tip = mealCost * (tipPercent / 100.0)
tax = mealCost * (taxPercent / 100.0)
totalCost = round(mealCost + tip + tax)

print(totalCost)
