class BMI(object):
    def __init__(self, W, H):
        self.W = W
        self.H = H

    def square(self):
        return self.H ** 2

    def div(self):
        return self.W / self.square() * 10000

    def get_BMI(self):
        result = int(self.div())
        bmi = ''
        if result >= 30:
            bmi = '당신은 비만 범주에 속합니다. 꾸준한 운동과 건강한 식단을 지켜주세요.'

        elif result >= 25:
            bmi = '당신은 과체중 범주에 속합니다. 당신은 많은 체지방 혹은 근육을 가지고 있습니다. 꾸준한 운동과 건강한 식단을 지켜주세요.'

        elif result >= 18.5:
            bmi = '당신은 정상 체중 범주에 속합니다. 앞으로도 잘해주세요!'

        else:
            bmi = '당신은 저체중 범주에 속합니다. 충분한 영양 공급 또는 의사와의 상담을 통해 정상체중을 유지해주세요.'

        return bmi

    @staticmethod
    def main():
        B = BMI(int(input('몸무게 입력(kg)')), int(input('키 입력(cm)')))

        print(f'bmi지수 : {B.div()}')
        print(f'결과 : {B.get_BMI()}')

BMI.main()


