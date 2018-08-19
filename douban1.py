import requests, codecs

from lxml import html

import time

import random

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}

f_cookies = open('cookie.txt', 'r')

cookies = {}

for line in f_cookies.read().split(';'):
    name, value = line.strip().split('=', 1)

    cookies[name] = value

# print(cookies)


for num in range(0, 10000, 20):

    url = 'https://movie.douban.com/subject/24852545/comments?start=' + str(

        num) + '&amp;limit=20&amp;sort=new_score&amp;status=P&amp;percent_type='
    print(url)

    with codecs.open('comment.txt', 'a', encoding='utf-8') as f:

        try:

            r = requests.get(url, headers=header, cookies=cookies)

            result = html.fromstring(r.text)

            comment = result.xpath(" // div[@class ='comment'] / p / span / text() ")

            for i in comment:
                f.write(i.strip() + '\r\n')

        except Exception as e:

            print(e)

    time.sleep(1 + float(random.randint(1, 100)) / 20)
