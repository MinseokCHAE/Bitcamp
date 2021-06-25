from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random


class Service(object):

    def __init__(self):
        self.text = open('./raw_data/alice.txt').read()
        self.image = np.array(Image.open('./raw_data/alice_mask.png'))
        self.image_colors = ImageColorGenerator(self.image)
        self.stopwords = set(STOPWORDS)
        self.wordcloud = WordCloud(background_color='white', mask=self.image, stopwords=self.stopwords)

    def image_color(self):
        pass

    def stopwords_set(self):
        self.stopwords.add('said')

    def wordcloud_generate(self):
        self.wordcloud.generate(self.text)
        self.wordcloud.to_file('./saved_data/alice.png')

    def wordcloud_show(self):
        plt.imshow(self.wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.figure()
        plt.imshow(self.image, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def wordcloud_show_grey(self):
        pass


if __name__ == '__main__':

    s = Service()

    while 1:
        menu = int(input('0.exit 1.기본이미지 2.기본이미지+grey 3.다른이미지+색상반영'))

        if menu == 0:
            break

        elif menu == 1:
            s.image_color()
            s.stopwords_set()
            s.wordcloud_generate()
            s.wordcloud_show()

        elif menu == 2:
            pass

        elif menu == 3:
            pass

        else:
            print('잘못된입력')
            continue


'''
text = open('./raw_data/alice.txt').read()
alice_mask = np.array(Image.open('./raw_data/alice_mask.png'))
image_colors = ImageColorGenerator(alice_mask)

stopwords = set(STOPWORDS)
stopwords.add('said')

wc = WordCloud(background_color='white', mask=alice_mask, stopwords=stopwords)
wc.generate(text)
wc.to_file('./saved_data/alice.png')

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
