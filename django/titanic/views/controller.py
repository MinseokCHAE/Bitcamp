from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    d = Dataset()
    s = Service()

    def modeling(self, train, test) -> object:
        s = self.s
        this = self.preprocessing(train, test)
        this.label = s.create_label(this)
        this.train = s.create_train(this)
        return this

    def preprocessing(self, train, test) -> object:
        s = self.s
        this = self.d
        this.train = s.new_model(train)
        this.test = s.new_model(test)
        print(f'train type : {type(this.train)}')
        print(f'train column : {this.train.columns}')
        print(f'test type : {type(this.test)}')
        print(f'test column : {this.test.columns}')
        return this
