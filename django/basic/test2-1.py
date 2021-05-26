'''
단을 입력받아서, 입력받은 단의 1~9 곱을 출력
단은 정수
'''

class Gugudan(object):

    list = []
    x = ''

    def gugudan_create(self):
        x = int(input('단 입력'))
        for i in range(1, 9):
            self.list.append(x * i)
            return self.list

    def gugudan_read(self):
        print(self.list)


    @staticmethod
    def main():
        g = Gugudan()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.update 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                g.gugudan_create()

            elif menu == 2:
                g.gugudan_read()

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue

Gugudan.main()
