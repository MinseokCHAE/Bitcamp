
from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''
    class_name = []

    def __str__(self):
        return self.url

    def get_ranking(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 0
        print('<Artist>')
        for link in soup.find_all(name='p', attrs=({"class": self.class_name[0]})):
            count += 1
            print(f"{str(count)}위")
            print(f"{self.class_name[0]} : {link.find('a').text}")
        print('<Title>')
        for link in soup.find_all(name='p', attrs=({"class": self.class_name[1]})):
            count += 1
            print(f"{str(count)}위")
            print(f"{self.class_name[1]} : {link.find('a').text}")


# URL : https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()

        while 1:
            menu = int(input('0.Exit 1.Input URL 2.Get Ranking'))

            if menu == 0:
                break

            elif menu == 1:
                bugs.url = input('URL 입력')

            elif menu == 2:
                bugs.class_name.append('artist')
                bugs.class_name.append('title')

                bugs.get_ranking()

            elif menu == 3:
                pass

            else:
                print('잘못된 입력')
                continue


BugsMusic.main()
