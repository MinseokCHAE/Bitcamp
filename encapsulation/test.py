
class Info(object):

    def __init__(self, name, address, year):
        self.name = name
        self.address = address
        self.year = year

    def name(self):
        return self.name

    def address(self):
        return self.address

    def sub(self):
        return 2021 - int(self.year)

    @staticmethod
    def main():
        I = Info(input('이름을 입력하세요'), input('주소를 입력하세요'), int(input('출생년도를 입력하세요(네자리)')))

        print(f'이름 : {I.name()}')
        print(f'주소 : {I.address()}')
        print(f'나이 : {I.sub()}')

Info.main()
