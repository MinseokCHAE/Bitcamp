import pandas as pd

class MyDataFrame(object):

    def __init__(self, columns, index):
        self.columns = columns
        self.index = index

    @staticmethod
    def main():
        m = MyDataFrame()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.update 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                pass

            elif menu == 1:
                pass

            elif menu == 1:
                pass

            elif menu == 1:
                pass

            else:
                print('잘못된입력')
                continue

MyDataFrame.main()
