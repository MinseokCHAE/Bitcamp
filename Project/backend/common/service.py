from common.abstracts import PrinterBase, ReaderBase
import json
import pandas as pd


class Printer(PrinterBase):

    def print(self, dto):
        print('*' * 100)
        print('Check')
        print('*' * 100)
        print(f'1. type \n {type(dto)} ')
        print(f'2. column \n {dto.columns} ')
        print(f'3. head \n {dto.head()} ')
        print(f'4. null \n {dto.isnull().sum()} ')
        print('*' * 100)


class Reader(ReaderBase):

    def new_file(self, file) -> str:
        return file._context + file._fname

    def csv(self, file) -> object:
        df = pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=',')
        return df

    def xls(self, file, header, usecols) -> object:
        df = pd.read_excel(f'{self.new_file(file)}.xls', encoding='UTF-8', header=header, usecols=usecols)
        return df

    def json(self, file) -> object:
        df = json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))
        return df

    def create_gmaps(self):
        pass
