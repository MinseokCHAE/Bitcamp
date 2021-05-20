
class Fourcal():
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def add(self):
        return a.first + a.second


    def sub(self):
        result = a.first - a.second
        return result

    def mul(self):
        result = a.first * a.second
        return result

    def div(self):
        result = a.first / a.second
        return result


if __name__ == '__main__':
    c = Fourcal()

    a = c

    a.setdata(12, 4)

    print(a.first + a.second)
    print(a.second - a.first)
    print(a.first * a.second)
    print(a.first / a.second)

    print(a.add())
    print(a.sub())
    print(a.mul())
    print(a.div())




