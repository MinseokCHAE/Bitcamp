
class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'Stock({self.name}, {self.code})'


    @staticmethod
    def main():
        list = []
        while 1:
            menu = int(input('0. 프로그램 종료 1. 종목추가 2. 출력 3. 삭제'))
            if menu == 0:
                break

            elif menu == 1:
                list.append(Stock(input('종목명을 입력하세요'), input('종목코드를 입력하세요')))

            elif menu == 2:
                for j in list:
                    print(f'출력결과 \n {j.get_stock()}')

            elif menu == 3:
                del_name = input('삭제할 종목명을 입력하세요')
                for i, j in enumerate(list):
                    if j.name == del_name:
                        del list(i)

            else:
                print('잘못된 입력입니다.')
                continue

Stock.main()
