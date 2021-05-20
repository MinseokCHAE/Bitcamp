
class CalculatorConstructor:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


if __name__ == '__main__':
    c = CalculatorConstructor(12,4)


    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())

    



















