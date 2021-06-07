from title.models.dataset import Dataset
import pandas as pd


class Service(object):

    d = Dataset()

    def new_model(self, payload):
        context = self.d.context = './data/'
        fname = self.d.fname = payload
        return pd.read_excel(context + fname + '.xlsx', sheet_name='평균전세')
