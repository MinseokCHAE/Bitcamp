from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    d = Dataset()
    s = Service()

    def modeling(self, train) -> object:
        s = self.s

    def preprocessing(self, train) -> object:
        s = self.s
        this = self.d
        this.train = s.new_model(train)
        print(f'train type : {type(this.train)}')
        print(f'train column : {this.train.columns}')
        print(f'train 상위5개 data : {this.train.head()}')
        print(f'train 하위5개 data : {this.train.tail()}')
