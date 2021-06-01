from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    d = Dataset()

    def new_model(self, payload):
        this = self.d
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train['Embarked'] = this.train['Embarked'].map(mapping)
        this.test['Embarked'] = this.test['Embarked'].map(mapping)
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        feature1 = ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme']
        feature2 = ['Countess', 'Lady', 'Sir']
        mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
            dataset['Title'] = dataset['Title'].replace(feature1, 'Rare')
            dataset['Title'] = dataset['Title'].replace(feature2, 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(mapping)
        return this

    @staticmethod
    def gender_nominal(this) -> object:
        combine = [this.train, this.test]
        mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(mapping)
        return this

    @staticmethod
    def drop_feature(this) -> object:
        feature = ['Cabin', 'Ticket', 'Name', 'Sex']
        this.train = this.train.drop(feature, axis=1)
        this.test = this.test.drop(feature, axis=1)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        return

    @staticmethod
    def create_k_fold_nominal(this) -> object:
        return

    @staticmethod
    def fare_ordinal(this) -> object:
        return

    @staticmethod
    def fare_band_fill_na(this) -> object:
        return

