
class CalculatorStatic(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    @staticmethod
    def main():
        CS = CalculatorStatic(int(input('첫번째수 입력')), int(input('두번째수 입력')))

        print(f'{CS.a} + {CS.b} = {CS.add()}')
        print(f'{CS.a} - {CS.b} = {CS.sub()}')
        print(f'{CS.a} * {CS.b} = {CS.mul()}')
        print(f'{CS.a} / {CS.b} = {CS.div()}')


CalculatorStatic.main()
