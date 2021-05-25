
from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url

    def get_ranking(self, class_name):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        count = 0
        print('<Artist>')
        for link in soup.find_all(name='p', attrs=({"class": class_name[0]})):
            count += 1
            print(f"{str(count)}위")
            print(f"{class_name[0]} : {link.find('a').text}")
        print('<Title>')
        for link in soup.find_all(name='p', attrs=({"class": class_name[1]})):
            count += 1
            print(f"{str(count)}위")
            print(f"{class_name[1]} : {link.find('a').text}")


#https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01
    @staticmethod
    def main():
        bugs = BugsMusic()

        while 1:
            menu = int(input('0.Exit 1.Input URL 2.Title or Artist'))

            if menu == 0:
                break

            elif menu == 1:
                url = input('URL 입력')

            elif menu == 2:
                bugs.get_ranking(url, ['artist', 'title'])

            elif menu == 3:
                pass

            else:
                print('잘못된 입력')
                continue


BugsMusic.main()
