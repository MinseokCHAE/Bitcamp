from real_estate.service import HousingService
from common.service import CommonService


class HousingAPI(CommonService):

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.exit 1.create DF 2. 3. 4.'))

            if menu == 0:
                break

            elif menu == 1:
                HousingService().print(HousingService().new_model('housing'))

            elif menu == 2:
                pass

            else:
                print('wrong input')
                continue

HousingAPI.main()