
from title.models.dataset import Dataset
from title.models.service import Service
from title.templates.plot import Plot


if __name__ == '__main__':

    while 1:
        menu = int(input('0.exit\n'
                         '1.모델생성\n'
                         '2.df생성\n'
                         '3.\n'
                         '4.'))
        if menu == 0:
            break

        elif menu == 1:
            Service()

        elif menu == 2:
            pass

        elif menu == 3:
            pass

        elif menu == 4:
            pass

        else:
            print('잘못된입력')
            continue
