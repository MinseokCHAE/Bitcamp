from crime_cctv.models import cctvDTO
import pandas as pd


class cctvService(object):
    dto = cctvDTO()

    def new_models(self, payload):
        context = self.dto.context = './data/'
        fname = self.dto.fname = payload


        df =
        return df