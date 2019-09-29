class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, number):
        sum = 1

        for divisor in range(2, number):
            if divisor * divisor > number: break
            (freq, number) = self.findDivCount(number, divisor)
            sum *= (divisor ** (freq + 1) - 1) / (divisor - 1)

        if number != 1:
            sum *= ((number ** 2) - 1) / (number - 1)

        return int(sum)

    def findDivCount(self, val, div):
        freq = 0

        while val % div == 0:
            freq += 1
            val /= div

        return (freq, val)



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)