
class Contacts(object):

    def __init__(self, name, number, mail, address):
        self.name = name
        self.number = number
        self.mail = mail
        self.address = address

    def get_info(self):
        return f'이름 : {self.name}, 전화번호 : {self.number}, ' \
               f'이메일 : {self.mail}, 주소 : {self.address}'


    @staticmethod
    def main():
        list = []
        while 1:
            menu = int(input('0. 프로그램 종료 1. 주소록 추가 2. 출력 3. 삭제'))
            if menu == 0:
                break

            elif menu == 1:
                list.append(Contacts(input('이름을 입력하세요'), input('전화번호를 입력하세요'),
                             input('이메일을 입력하세요'), input('주소를 입력하세요')))

            elif menu == 2:
                for j in list:
                    print(f'출력결과 : {j.get_info()}')

            elif menu == 3:
                del_name = input('삭제할 이름')
                for i, j in enumerate(list):
                    if j.name == del_name:
                        del list[i]

            else:
                print('잘못된 입력입니다.')
                continue

Contacts.main()
