from titanic.views.controller import Controller
from titanic.models.dataset import Dataset
from titanic.models.service import Service
from titanic.templates.plot import Plot


if __name__ == '__main__':

    while 1:
        menu = int(input('0.exit\n'
                         '1.data visualization\n'
                         '2.modeling\n'
                         '3.machine learning\n'
                         '4.submit'))
        if menu == 0:
            break

        elif menu == 1:
            Plot('train.csv').draw_survived_dead()
            Plot('train.csv').draw_sex()
            Plot('train.csv').draw_pclass()
            Plot('train.csv').draw_embarked()

        elif menu == 2:
            Controller().modeling('train.csv', 'test.csv')

        elif menu == 3:
            Controller().learning('train.csv', 'test.csv')

        elif menu == 4:
            Controller().submit('train.csv', 'test.csv')

        else:
            print('잘못된입력')
            continue
