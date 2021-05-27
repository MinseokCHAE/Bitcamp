import pandas as pd

class Conversion(object):

    ls = []
    tp = ()
    dt = {}
    df = None
    i = 0   # int
    f = 0.0     # float
    s = ''  # str

    def conversion_1(self):
        self.tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print(self.tp)
        print(f'타입 : {type(self.tp)}')

    def conversion_2(self):
        self.ls = list(self.tp)
        print(self.ls)
        print(f'타입 : {type(self.ls)}')

    def conversion_3(self):
        self.ls = [float(i) for i in self.ls]
        #self.ls = list(map(float, self.ls))
        print(self.ls)
        print(f'타입 : {type(self.ls)}')

    def conversion_4(self):
        self.ls = [int(i) for i in self.ls]
        #self.ls = list(map(int, self.ls))
        print(self.ls)
        print(f'타입 : {type(self.ls)}')

    def conversion_5(self):
        '''
        for i, x in enumerate(self.ls):
            self.dt[str(self.ls[i])] = self.ls[i]
        '''
        self.dt = dict(zip([str(i) for i in self.ls], self.ls))
        #self.dt = {str(self.ls[i]): self.ls[i] for i in range(0, 10)}
        #self.dt = {str(self.ls[i]): self.ls[i] for i, x in enumerate(self.ls)}
        print(self.dt)
        print(f'타입 : {type(self.dt)}')

    def conversion_6(self):
        self.tp = tuple(list('hello'))
        print(self.tp)
        print(f'타입 : {type(self.tp)}')

    def conversion_7(self):
        self.ls = list(self.tp)
        print(self.ls)
        print(f'타입 : {type(self.ls)}')

    def conversion_8(self):
        self.df = pd.DataFrame.from_dict(self.dt, orient='index')
        print(self.df)
        print(f'타입 : {type(self.df)}')

    @staticmethod
    def main():
        c = Conversion()

        while 1:
            menu = int(input('0.exit 1. 2. 3. 4. 5. 6. 7'))

            if menu == 0:
                break

            elif menu == 1:     # (1~10) tp1 추가
                c.conversion_1()

            elif menu == 2:     # tp1 -> ls2
                c.conversion_2()

            elif menu == 3:     # ls2 -> ls3(float)
                c.conversion_3()

            elif menu == 4:     # ls3 -> ls4(int)
                c.conversion_4()

            elif menu == 5:     # ls4 ->dt5 key = index, str
                c.conversion_5()

            elif menu == 6:     # 'hello' -> tp6
                c.conversion_6()

            elif menu == 7:     # tp6 -> ls7
                c.conversion_7()

            elif menu == 8:     # dt5 -> df
                c.conversion_8()

            else:
                print('잘못된입력')
                continue

Conversion.main()
