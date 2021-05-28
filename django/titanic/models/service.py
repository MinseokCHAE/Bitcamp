from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    d = Dataset()

    def new_model(self, payload):
        this = self.d
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
