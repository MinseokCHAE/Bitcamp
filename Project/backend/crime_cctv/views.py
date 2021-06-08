from crime_cctv.models import cctvDTO
from crime_cctv.services import cctvService
from common.views import CommonView


class cctvApi(object):



    @staticmethod
    def main():
        while 1:
            menu = int(input('0.exit 1.create DF 2. 3. 4.'))

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
                print('wrong input')
                continue

cctvApi.main()
