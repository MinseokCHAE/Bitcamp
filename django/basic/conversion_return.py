import pandas as pd

class Conversion(object):

    @staticmethod
    def conversion_1() -> ():
        return (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    @staticmethod
    def conversion_2(tp) -> []:
        return list(tp)

    @staticmethod
    def conversion_3(ls) -> []:
        return (float(i) for i in ls)
        #return list(map(float, ls))

    @staticmethod
    def conversion_4(ls) -> []:
        return [int(i) for i in ls]
        #return list(map(int, ls))

    @staticmethod
    def conversion_5(ls) -> {}:
        return dict(zip([str(i) for i in ls], ls))
        #return {str(ls[i]): ls[i] for i in range(0, 9)}
        #return {str(ls[i]): ls[i] for i, x in enumerate(ls)}

    @staticmethod
    def conversion_6() -> ():
        return tuple(list('hello'))

    @staticmethod
    def conversion_7(tp) -> []:
        return list(tp)

    @staticmethod
    def conversion_8(dt) -> object:
        return pd.DataFrame.from_dict(dt, orient='index')

    @staticmethod
    def main():
        c = Conversion()
        ls = []
        tp = ()
        dt = {}
        df = None
        i = 0  # int
        f = 0.0  # float
        s = ''  # str

        while 1:
            menu = int(input('0.exit 1. 2. 3. 4. 5. 6. 7, 8'))

            if menu == 0:
                break

            elif menu == 1:     # (1~10) tp1 추가
                tp = c.conversion_1()
                print(tp)
                print(f'타입 : {type(tp)}')

            elif menu == 2:     # tp1 -> ls2
                ls = c.conversion_2(tp)
                print(ls)
                print(f'타입 : {type(ls)}')

            elif menu == 3:     # ls2 -> ls3(float)
                ls = c.conversion_3(ls)
                print(ls)
                print(f'타입 : {type(ls)}')

            elif menu == 4:     # ls3 -> ls4(int)
                ls = c.conversion_4(ls)
                print(ls)
                print(f'타입 : {type(ls)}')

            elif menu == 5:     # ls4 ->dt5 key = index, str
                dt = c.conversion_5(ls)
                print(dt)
                print(f'타입 : {type(dt)}')

            elif menu == 6:     # 'hello' -> tp6
                tp = c.conversion_6()
                print(tp)
                print(f'타입 : {type(tp)}')

            elif menu == 7:     # tp6 -> ls7
                ls = c.conversion_7(tp)
                print(ls)
                print(f'타입 : {type(ls)}')

            elif menu == 8:     # dt5 -> df
                df = c.conversion_8(dt)
                print(df)
                print(f'타입 : {type(df)}')

            else:
                print('잘못된입력')
                continue

Conversion.main()
