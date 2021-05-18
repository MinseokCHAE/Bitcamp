class BMI() :
    def setdata(self, weight, height):
        self.weight = weight
        self.height = height

    def square(self):
        return self.height ** 2

    def div(self):
        return self.weight / self.square() * 10000

if __name__ == '__main__':
    b = BMI()
    b.setdata(65, 181)

    print(b.square())
    print(b.div())




