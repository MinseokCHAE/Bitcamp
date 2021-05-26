'''
단을 입력받아서, 입력받은 단의 1~9 곱을 출력
단은 정수
'''

class Gugudan(object):

    x = 0
    dict = {}

    def gugudan_create_1(self):
        for i in range(1, 10):
            print(f'{self.x} * {i} = {self.x * i}')

    def gugudan_create_all(self):
        pass

    def gugudan_create_dict(self):
        for i in range(1, 10):
            self.dict[i] = self.x * i
        print('dict 출력')
        print(self.dict)
        for k in self.dict.keys():
            print(f'{self.x} * {k} = {self.dict.get(k)}')


    @staticmethod
    def main():
        g = Gugudan()

        while 1:
            menu = int(input('0.exit 1.1 2.all 3.dict 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                g.x = int(input('단 입력'))
                g.gugudan_create_1()

            elif menu == 2:
                g.gugudan_create_all()

            elif menu == 3:
                g.x = int(input('단 입력'))
                g.gugudan_create_dict()

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue

Gugudan.main()
