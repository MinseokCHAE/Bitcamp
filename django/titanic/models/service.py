from titanic.models.dataset import Dataset
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


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
        combine = [this.train, this.test]
        mapping = {'S': 1, 'C': 2, 'Q': 3}
        for dataset in combine:
            dataset['Embarked'] = dataset['Embarked'].fillna('S')
            dataset['Embarked'] = dataset['Embarked'].map(mapping)
        return this

        #this.train = this.train.fillna({'Embarked': 'S'})
        #this.test = this.test.fillna({'Embarked': 'S'})

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
    def age_ordinal(this) -> object:
        combine = [this.train, this.test]
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for dataset in combine:
            dataset['Age'] = dataset['Age'].fillna(-0.5)
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)
            dataset['AgeGroup'] = dataset['AgeGroup'].map(mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        combine = [this.train, this.test]
        bins = [-1, 8, 15, 31, np.inf]  # pd.qcut(this.train['Fare'], q=4)
        labels = ['A', 'B', 'C', 'D']
        mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
        for dataset in combine:
            dataset['Fare'] = dataset['Fare'].fillna(0)
            dataset['FareBand'] = pd.cut(dataset['Fare'], bins=bins, labels=labels)
            dataset['FareBand'] = dataset['FareBand'].map(mapping)
        return this

    @staticmethod
    def drop_feature(this) -> object:
        feature = ['Cabin', 'Ticket', 'Name', 'Sex', 'Age', 'Fare']
        this.train = this.train.drop(feature, axis=1)
        this.test = this.test.drop(feature, axis=1)
        return this

        #combine = [this.train, this.test]
        #feature = ['Cabin', 'Ticket', 'Name', 'Sex', 'Age']
        #for dataset in combine:
            #dataset.drop(feature, axis=1)

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(SVC(), this.train, this.label, cv=KFold(n_splits=10, shuffle=True, random_state=0),
                                n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
