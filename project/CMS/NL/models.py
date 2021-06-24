from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


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
