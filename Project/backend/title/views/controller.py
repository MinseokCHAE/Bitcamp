from title.models.service import Service
from title.models.dataset import Dataset


class Controller(object):

    s = Service()
    d = Dataset()

    def preprocessing(self, housing) -> object:
        s = self.s
        housing =s.new_model(housing)

        Controller.print(d.s)

    @staticmethod
    def print(self.d)
        #print('*' * 100)
        #print('<CHECK>')
        #print('*'*100)
        #print(f'TRAIN TYPE : \n{type(this.train)}')
        #print(f'TRAIN COLUMN : \n{this.train.columns}')
        #print(f'TRAIN HEAD : \n{this.train.head()}')
        #print(f'TRAIN NULL COUNT : \n{this.train.isnull().sum()}')
        #print('*' * 100)


