
class Grade(object):

    def __init__(self, K, E, M):
        self.K = K
        self.E = E
        self.M = M

    def sum(self):
        return self.K + self.E + self.M

    def avr(self):
        return self.sum() / 3

    def get_grade(self):
        score = int(self.avr())
        grade = ''
        if score >= 90:
            grade = 'A'

        elif score >= 80:
            grade = 'B'

        elif score >= 70:
            grade = 'C'

        elif score >= 60:
            grade = 'D'

        else:
            grade = 'F'

        return grade

    @staticmethod
    def main():
        G = Grade(int(input('국어 점수 입력')), int(input('영어 점수 입력')),
                               int(input('수학 점수 입력')))

        print(f'총점 : {G.sum()}')
        print(f'평균 : {G.avr()}')
        print(f'학점 : {G.get_grade()}')

Grade.main()
