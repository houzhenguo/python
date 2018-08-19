
import random

import numpy as np

import pandas as pd

from pyecharts import WordCloud

import matplotlib.pyplot as plt

from PIL import Image,ImageSequence

from wordcloud import WordCloud,ImageColorGenerator

def DrawWordcloud(read_name):

    image = Image.open('src.jpg')#作为背景形状的图

    graph = np.array(image)

    #参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状

    wc = WordCloud(font_path = 'C:\\windows\\Fonts\\simhei.ttf', background_color = 'White', max_words = 50, mask = graph)

    fp = pd.read_csv(read_name)#读取词频文件

    name = list(fp.name)#词

    value = fp.val#词的频率

    for i in range(len(name)):

      name[i] = str(name[i])

      #注意因为要显示中文，所以需要转码

      name[i] = name[i].decode('gb2312')

    dic = dict(zip(name, value))#词频以字典形式存储

    wc.generate_from_frequencies(dic)#根据给定词频生成词云

    image_color = ImageColorGenerator(graph)

    plt.imshow(wc)

    plt.axis("off")#不显示坐标轴

    plt.show()

    wc.to_file('Wordcloud.png')#保存的图片命名为Wordcloud.png

if __name__=='__main__':

    DrawWordcloud("price.csv")
