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

        # 초기 모델 생성
        this.train = s.new_model(train)
        this.test = s.new_model(test)

        # nominal, ordinal 로 졍형화
        this = s.embarked_nominal(this)
        this = s.title_nominal(this)
        this = s.gender_nominal(this)

        # 불필요한 feature (Cabin, Ticket, Name) 제거
        this = s.drop_feature(this)

        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):
        print('<Type&Column&Head Checking>')
        print('*'*100)
        print(f'train type : {type(this.train)}')
        print(f'train column : {this.train.columns}')
        print(f'train head : {this.train.head()}')
        print('*' * 100)
        print(f'test type : {type(this.test)}')
        print(f'test column : {this.test.columns}')
        print(f'test head : {this.test.head()}')
        print('*' * 100)

