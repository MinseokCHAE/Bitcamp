
class GradeConstructor:

    def __init__(self, Kor, Eng, Math):
        self.Kor = Kor
        self.Eng = Eng
        self.Math = Math

    def sum(self):
        return self.Kor + self.Eng + self.Math

    def avr(self):
        return  self.sum() / 3


if __name__ == '__main__':
    g = GradeConstructor(99, 98, 97)


    print(g.sum())
    print(g.avr())


