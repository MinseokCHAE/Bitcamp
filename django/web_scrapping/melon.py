
from bs4 import BeautifulSoup
import requests

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent' : 'Mozilla/5.0'}
    class_name = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        bs = BeautifulSoup(self.url, 'lxml')
        count = 0
        print('------곡명------')
        for i in bs.find_all('div', {'class':self.class_name[0]}):
            count += 1
            print(f"{str(count)}위")
            print(f'{i.find("a").text}')
        print('------가수명------')
        for i in bs.find_all('div', {'class': self.class_name[1]}):
            count += 1
            print(f"{str(count)}위")
            print(f'{i.find("a").text}')


    @staticmethod
    def main():
        m = Melon()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.update 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                m.set_url(input('time 입력 예) 2021052511'))

            elif menu == 2:
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue


Melon.main()
