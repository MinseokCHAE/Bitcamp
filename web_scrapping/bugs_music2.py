
from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):

    url = ''

    def __str__(self):
        return self.url


    @staticmethod
    def get_ranking():
        bugs = BugsMusic()
        soup = BeautifulSoup(urlopen(bugs.url), 'lxml')
        xx = input('pass')
        count = 0
        for link in soup.find_all(name='p', attrs=({"class": xx})):
            count += 1
            print(f"{str(count)}위")
            print(f"{xx} : {link.find('a').text}")


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
                BugsMusic.get_ranking()

            elif menu == 3:
                BugsMusic.get_ranking()

            else:
                print('잘못된 입력')
                continue


BugsMusic.main()
