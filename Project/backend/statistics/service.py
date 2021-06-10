from common.model import DataTransferObject
from common.service import Printer, Reader
from common.abstracts import ReaderBase


class StatisticsService(ReaderBase):

    def new_file(self, payload):
        DataTransferObject().context = payload.get('context')
        DataTransferObject().fname = payload.get('fname')

    def csv(self, payload):
        DataTransferObject().context = payload.get('context')
        DataTransferObject().fname = payload.get('fname')
        Printer().print(Reader().csv(DataTransferObject()))

    def xls(self):
        pass

    def json(self):
        pass
