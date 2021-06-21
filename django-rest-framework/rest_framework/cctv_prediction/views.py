from rest_framework.cctv_prediction.services import Service
from rest_framework.common.services import Reader, Printer
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


class StatisticsAPI(object):

    @staticmethod
    def main():
        while 1:
            menu = int(input('0.exit 1.cctv in Seoul 2.crime in Seoul 3. 4.'))

            if menu == 0:
                break

            elif menu == 1:
                Service().csv({'context': './data/', 'fname': 'cctv_in_seoul'})

            elif menu == 2:
                pass

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('wrong input')
                continue


StatisticsAPI.main()
