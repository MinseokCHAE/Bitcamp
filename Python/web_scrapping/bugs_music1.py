

class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url


    @staticmethod
    def main():
        bugs = BugsMusic()

        while 1:
            menu = int(input(' 0.Exit 1.Input URL 2.Print URL 3.Update 4.Delete'))
            if menu == 0:
                break

            elif menu == 1:
                bugs = BugsMusic(input('URL 입력'))

            elif menu == 2:
                print(f'URL : {bugs}')

            elif menu == 3:
                pass

            elif menu == 4:
                pass

            else:
                print('잘못된 입력.')
                continue


BugsMusic.main()
