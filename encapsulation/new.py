class BMI() :
    def setdata(self, weight, height):
        self.weight = weight
        self.height = height

    def sum(self):
        return self.weight + self.height

    def square(self):
        return self.height * self.height
        return self.height ^ 2


    def div(self):
        return self.weight / self.square()



if __name__ == '__main__':
    b = BMI()
    b.setdata(65, 1.81)

    print(b.sum())
    print(b.square())
    print(b.div())




