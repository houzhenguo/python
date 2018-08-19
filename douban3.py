# coding=utf-8

import matplotlib.pyplot as plt

from scipy.misc import imread

from wordcloud import WordCloud

import jieba, codecs

from collections import Counter

text = codecs.open('comment.txt', 'r', encoding='utf-8').read()


text_jieba = list(jieba.cut(text))

c = Counter(text_jieba)  # 计数
word = c.most_common(500)  # 取前500

bg_pic = imread('src.jpg')

wc = WordCloud(

    #font_path='C:\Windows\Fonts\微软雅黑.TTF',  # 指定中文字体

    background_color='white',  # 设置背景颜色

    max_words=2000,  # 设置最大显示的字数

    mask=bg_pic,  # 设置背景图片

    max_font_size=200,  # 设置字体最大值

    random_state=20  # 设置多少种随机状态，即多少种配色

)
wc.generate_from_frequencies(dict(word))  # 生成词云
print(dict(word))


wc.to_file('result.jpg')

# show

plt.imshow(wc)

plt.axis("off")

plt.figure()

plt.imshow(bg_pic, cmap=plt.cm.gray)

plt.axis("off")

plt.show()
