
class Account(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def random_account(self):
        pass

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = int(input('0. 프로그램 종료, 1. 계좌추가, 2. 출력'))
            if menu == 0:
                break

            elif menu == 1:
                ls.append(Account(input('예금주명을 입력하세요'), input('입금 금액을 입력하세요')))

            elif menu == 2:
                print('은행명 : SC 은행 \n계좌번호 : {}')

            else:
                print('잘못된 입력입니다.')
                continue

Account.main()
