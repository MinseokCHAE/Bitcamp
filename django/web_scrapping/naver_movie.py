import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup


class NaverMovie(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ''
    ls = []
    dt = {}
    df = None

    def get_rank(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)

        bs = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = bs.find_all('div', {'class': input('class_name')}) #tit3
        self.ls = [i.find('a').text for i in all_div]

        driver.close()

        for i, j in enumerate(self.ls):
            self.dt[i+1] = self.ls[i]
        #self.dt = {self.ls[i]: self.ls[j] for i, j in enumerate(self.ls)}

        self.df = pd.DataFrame.from_dict(self.dt, orient='index')

        path = './data/movie.csv'
        self.df.to_csv(path, sep=',', na_rep='nan')

        print(self.df)


if __name__ == '__main__':
    NaverMovie().get_rank()