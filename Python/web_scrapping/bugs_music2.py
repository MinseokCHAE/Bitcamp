
from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url


    @staticmethod
    def get_ranking():
        bugs = BugsMusic()

        xx = input('pass')


#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()

        while 1:
            menu = int(input('0.Exit 1.Input URL 2.Title or Artist'))

            if menu == 0:
                break

            elif menu == 1:
                bugs.url = input('URL 입력')

            elif menu == 2:
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
                count = 0
                for link in soup.find_all(name='p', attrs=({"class": "artist"})):
                    count += 1
                    print(f"{str(count)}위")
                    print(f"artist : {link.find('a').text}")

            elif menu == 3:
                BugsMusic.get_ranking()

            else:
                print('잘못된 입력')
                continue


BugsMusic.main()
