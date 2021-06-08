from real_estate.models import HousingDTO
import pandas as pd
import xlwings as xw


class HousingService(object):
    dto = HousingDTO()

    # create DF
    def new_model(self, payload):
        context = self.dto.context = './data/'
        fname = self.dto.fname = payload
        # df = pd.read_excel(context + fname + '.xlsx', sheet_name='매매종합')
        sheet = xw.Book(context + payload + '.xlsx').sheets['매매종합']
        row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        df = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
        return df
