from real_estate.services import HousingService
from real_estate.models import HousingDTO
from common.views import CommonView


class HousingApi(CommonView):

    def print():

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.exit 1.create DF 2. 3. 4.'))

            if menu == 0:
                break

            elif menu == 1:
                HousingDTO().dframe = HousingService().new_model('housing')
                HousingApi.print(HousingDTO().dframe)

            elif menu == 2:
                pass

            else:
                print('wrong input')
                continue

HousingApi.main()