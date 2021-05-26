
from bs4 import BeautifulSoup
import requests

class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?dayTime='
    headers = {'User-Agent' : 'Mozilla/5.0'}
    class_name = []
    dict = {}
    title_ls = []
    artist_ls = []

    def set_url(self, time):
        self.url = requests.get(f'{self.url}{time}', headers=self.headers).text

    def get_ranking(self):
        bs = BeautifulSoup(self.url, 'lxml')
        ls1 = bs.find_all('div', {'class': self.class_name[1]})
        ls2 = bs.find_all('div', {'class': self.class_name[0]})
        for i in ls1:
            self.title_ls.append(i.find('a').text)
        for i in ls2:
            self.artist_ls.append(i.find('a').text)

    def insert_title_dict(self):
        for i in range(0, len(self.title_ls)):
            self.dict[self.title_ls[i]] = self.artist_ls[i]
        '''
        for i, j in enumerate(self.title_ls):
            self.dict[self.title_ls[i]] = self.artist_ls[i]

        for i, j in zip(self.title_ls, self.artist_ls):
            self.title_dict[i] = j
        '''''

    @staticmethod
    def main():
        m = Melon()

        while 1:
            menu = int(input('0.exit 1.create 2.read 3.dict 4.delete'))

            if menu == 0:
                break

            elif menu == 1:
                m.set_url(input('time ex)2021052511'))

            elif menu == 2:
                m.class_name.append('ellipsis rank01')
                m.class_name.append('ellipsis rank02')
                m.get_ranking()

            elif menu == 3:
                m.insert_title_dict()

            elif menu == 4:
                pass

            else:
                print('잘못된입력')
                continue


Melon.main()
