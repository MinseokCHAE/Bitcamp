from rest_framework.common.entities import FileDTO
from rest_framework.common.services import Reader, Printer, Scraper
from sklearn import preprocessing
from selenium import webdriver
from bs4 import BeautifulSoup
from glob import glob
import pandas as pd
import folium
import re
import numpy as np
'''
셀프 주유소는 정말 저렴할까?
'''


class Service(Reader, Scraper):

    def __init__(self):
        self.file = FileDTO()
        self.reader = Reader()
        self.printer = Printer()
        self.scraper = Scraper()

    def get_url(self):
        file = self.file
        reader = self.reader
        printer = self.printer
        scraper = self.scraper
        driver = scraper.driver()
        file.url = 'https://www.opinet.co.kr/searRgSelect.do'
        #print(driver.get(file.url))

        gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
        gu_list = gu_list_raw.find_elements_by_tag_name("option")

        gu_names = [option.get_attribute("value") for option in gu_list]
        gu_names.remove('')
        #print(gu_names)

    def gas_station_price_info(self):
        file = self.file
        reader = self.reader
        printer = self.printer
        station_files = glob('./raw_data/지역_위치별*xls')

        tmp_raw = []
        for i in station_files:
            t = pd.read_excel(i, header=2)
            tmp_raw.append(t)

        station_raw = pd.concat(tmp_raw)
        station_raw.info()
        #print('*' * 100)
        #print(station_raw.head(2))
        #print(station_raw.tail(2))

        stations = pd.DataFrame({'Oil_store': station_raw['상호'],
                                 '주소': station_raw['주소'],
                                 '가격': station_raw['휘발유'],
                                 '셀프': station_raw['셀프여뷰'],
                                 '상호': station_raw['상표']})
        #print('*' * 100)
        #print(stations.head(2))
        #print(stations.tail(2))

        stations['구'] = [i.split()[1] for i in stations['주소']]
        stations['구'].unique()
        stations[stations['구'] == '서울특별시'] = '성동구'
        stations['구'].unique()
        stations[stations['구'] == '특별시'] = '도봉구'
        stations['구'].unique()

        p = re.compile('^[0-9]+$')
        temp_stations = []
        for i in stations:
            temp_stations.append
        stations = stations[stations['가격'] != '^[0-9]+$']
        stations['가격'] = [float(i) for i in stations['가격']]
        stations.reset_index(inplace=True)
        del stations['index']
        #print('*' * 100)
        #print(stations.head(2))
        #print(stations.tail(2))


if __name__ == '__main__':
    s = Service()
    s.gas_station_price_info()
