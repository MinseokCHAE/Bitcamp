
class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_stock(self):
        return f'Stock({self.name}, {self.code})'


    @staticmethod
    def del_element(list, code):
        for i, j in enumerate(list):
            if j.code == code:
                del list[i]


    @staticmethod
    def main():
        list = []
        while 1:
            menu = int(input('0.종료 1.추가 2.출력 3.수정 4.삭제'))
            if menu == 0:
                break

            elif menu == 1:
                list.append(Stock(input('종목명을 입력하세요'), input('종목코드를 입력하세요')))

            elif menu == 2:
                for j in list:
                    print(f'출력결과 \n {j.get_stock()}')

            elif menu == 3:
                name = input('수정할 종목명을 입력하세요')
                for i, j in enumerate(list):
                    if j.name == name:
                        replace = Stock(input('새로운 종목명을 입력하세요'), j.code)
                        Stock.del_element(list, j.code)
                        list.append(replace)

            elif menu == 4:
                code = input('삭제할 종목코드를 입력하세요')
                Stock.del_element(list, code)

            else:
                print('잘못된 입력입니다.')
                continue

Stock.main()
