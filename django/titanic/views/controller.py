import pandas as pd
from titanic.models.dataset import Dataset
from titanic.models.service import Service
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


class Controller(object):

    d = Dataset()
    s = Service()

    def preprocessing(self, train, test) -> object:
        s = self.s
        this = self.d

        # 초기 모델 생성
        this.train = s.new_model(train)
        this.test = s.new_model(test)

        this.id = this.test['PassengerId']

        # nominal, ordinal 로 졍형화
        this = s.embarked_nominal(this)
        this = s.title_nominal(this)
        this = s.gender_nominal(this)

        this = s.age_ordinal(this)
        this = s.fare_ordinal(this)

        # 불필요한 feature 제거
        this = s.drop_feature(this)

        self.print_this(this)

        return this

    @staticmethod
    def print_this(this):

        print('*' * 100)
        print('<CHECK>')
        print('*'*100)
        print(f'TRAIN TYPE : \n{type(this.train)}')
        print(f'TRAIN COLUMN : \n{this.train.columns}')
        print(f'TRAIN HEAD : \n{this.train.head()}')
        print(f'TRAIN NULL COUNT : \n{this.train.isnull().sum()}')
        print('*' * 100)
        print(f'TEST TYPE : \n{type(this.test)}')
        print(f'TEST COLUMN : \n{this.test.columns}')
        print(f'TEST HEAD : \n{this.test.tail()}')
        print(f'TEST NULL COUNT : \n{this.test.isnull().sum()}')
        print('*' * 100)

    def modeling(self, train, test) -> object:
        s = self.s
        this = self.preprocessing(train, test)
        this.label = s.create_label(this)
        this.train = s.create_train(this)
        return this

    def learning(self, train, test):
        this = self.modeling(train, test)
        print(f' SVC Algorithm Accuracy {self.s.accuracy_by_svm(this)} %')

    def submit(self, train, test):
        this = self.modeling(train, test)
        clf = SVC()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)
