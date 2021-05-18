
class GradeStatic(object):

    def __init__(self, K, E, M):
        self.K = K
        self.E = E
        self.M = M

    def sum(self):
        return self.K + self.E + self.M

    def avr(self):
        return  self.sum() / 3

    @staticmethod
    def main():
        GS = GradeStatic(int(input('국어 점수 입력')), int(input('영어 점수 입력')),
                               int(input('수학 점수 입력')))

        print(f'{GS.K} + {GS.E} + {GS.M} = {GS.sum()}')
        print(f'{GS.sum()} / 3 = {GS.avr()}')

GradeStatic.main()



