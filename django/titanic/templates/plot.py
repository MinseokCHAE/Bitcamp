from titanic.models.dataset import Dataset
from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

class Plot(object):

    d: object = Dataset()
    s: object = Service()

    def __init__(self, fname):
        self.entity = self.s.new_model(fname)

    def draw_survived_dead(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0.사망자 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def draw_sex(self):
        this = self.entity
        f, ax = plt.subplots(1, 2, figsize = (18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1],
                                                                        shadow=True)
        ax[0].set_title('Survived male')
        ax[1].set_title('Survived female')
        plt.show()

    def draw_pclass(self):
        this = self.entity
        this['Survived'] = this['Survived'].replace(0, '사망').replace(1, '생존')
        this['Pclass'] = this['Pclass'].replace(1, '1').replace(2, '2').replace(3, '3')
        sns.countplot(data=this, x='Pclass', hue='Survived')
        plt.show()

    def draw_embarked(self):
        this = self.entity
        this['Survived'] = this['Survived'].replace(0, '사망').replace(1, '생존')
        this['Embarked'] = this['Embarked'].replace('S', 'S').replace('Q', 'Q').replace('C', 'C')
        sns.countplot(data=this, x='Embarked', hue='Survived')
        plt.show()


        #print(f'train type : {type(this)}')
        #print(f'train column : {this.columns}')
        #print(f'train 상위5개 data : {this.head()}')
        #print(f'train 하위5개 data : {this.tail()}')
