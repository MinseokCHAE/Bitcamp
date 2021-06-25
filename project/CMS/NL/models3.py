import pandas as pd
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class Data_Loading(object):

    urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt",
                               filename="ratings_train.txt")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt",
                               filename="ratings_test.txt")

    train_data = pd.read_table('./saved_data/ratings_train.txt')
    test_data = pd.read_table('./saved_data/ratings_test.txt')

    print('훈련용 리뷰 개수 :', len(train_data))
