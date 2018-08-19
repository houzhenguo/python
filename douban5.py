# coding=utf-8
from pyecharts import WordCloud
import jieba
with open('comment.txt', 'r', encoding='utf-8') as f:
    text_body = f.read()
f.close()

# 使用jieba进行分词
words_lst = jieba.cut(text_body.replace('\n', '').replace(' ', ''))
# 统计词频
total = {}
for i in words_lst:
    total[i] = total.get(i, 0) + 1

# 按词频进行排序，只选取包含两个或两个以上字的词
data = dict(sorted({k: v for k, v in total.items() if len(k) >= 2}.items(), \
                   key=lambda x: x[1], reverse=True)[:200])


name = data.keys()
value = [i for i in data.values()]
# 获取列表对象
# 构造一个词云对象，把所有的词放进去
word_cloud = WordCloud(width=1600, height=1024)
# pentagon表示用五角星的形状显示词云
word_cloud.add("", name, value, word_size_range=[20, 100], shape='triangle')
# 把词云显示到一个html网页中
word_cloud.render('content.html')


