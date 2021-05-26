
class Wikipedia(object):

    url = ''
    class_name = []
    headers = {}


    @staticmethod
    def main():
        w = Wikipedia()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.update 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                pass

            elif menu == 2:
                pass

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue

Wikipedia.main()
