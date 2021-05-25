
class Member(object):
    id = ''
    pw = ''
    name = ''
    email = ''

    def join(self):
        pass

    def login(self):
        pass

    def mypage(self):
        pass

    @staticmethod
    def main():
        m = Member()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.update 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                m.id = input('id 입력')
                m.id = input('pw 입력')
                m.id = input('name 입력')
                m.id = input('email 입력')

            elif menu == 2:
                print(f'ID:{m.id}')
                print(f'PW:{m.pw}')

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue


Member.main()
