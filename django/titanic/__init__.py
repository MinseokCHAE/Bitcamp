from titanic.views.controller import Controller


if __name__ == '__main__':
    c = Controller()

    while 1:
        menu = int(input('0.exit 1.print'))
        if menu == 0:
            break

        elif menu == 1:
            c.preprocessing('train.csv')

        else:
            print('잘못된입력')
            continue
