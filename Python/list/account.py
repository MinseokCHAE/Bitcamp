
import random

class Account(object):
    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC 은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def to_string(self):
        return f'은행명 : {self.BANK_NAME}, 예금주명 : {self.name}, 계좌번호 : {self.account_number}, 잔액 : {self.money}'


    @staticmethod
    def create_account_number():
        list = [str(random.randint(0, 9)) for i in range(3)]  # ??
        list.append('-')
        for i in range(2):
            list.append(str(random.randint(0, 9)))
        list.append('-')
        for i in range(6):
            list.append(str(random.randint(0, 9)))
        return ''.join(list)  # ??


    @staticmethod
    def del_account(list, account_number):
        for i, j in enumerate(list):
            if j.account_number == account_number:
                del list[i]


    @staticmethod
    def main():
        list = []
        while 1:
            menu = int(input('0.종료, 1.계좌개설, 2.계좌현황, 3.입출금, 4.계좌해지'))
            if menu == 0:
                break

            elif menu == 1:
                list.append(Account(Account.create_account_number(), input('예금주명'), input('금액(원)')))

            elif menu == 2:
                for i in list:
                    print(i.to_string())

            elif menu == 3:
                account_number = input('입출금할 계좌번호')
                money = input('입금할 금액(+-원)')
                for i, j in enumerate(list):
                    if j.account_number == account_number:
                        replace = Account(j.account_number, j.name, int(j.money) + int(money))
                        Account.del_account(list, account_number)
                        list.append(replace)

            elif menu == 4:
                Account.del_account(list, input('해지할 계좌번호'))

            else:
                print('잘못된 입력입니다.')
                continue

Account.main()
