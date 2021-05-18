class BMIConstructor:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def square(self):
        return self.height ** 2

    def div(self):
        return self.weight / self.square() * 10000

if __name__ == '__main__':
    b = BMIConstructor(65, 181)

    print(b.square())
    print(b.div())


