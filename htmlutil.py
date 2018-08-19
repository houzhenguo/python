import urllib.request
import re
def getHTML(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

html = getHTML("https://tieba.baidu.com/p/5352556650")
# ------ 修改html对象内的字符编码为UTF-8 ------
html = html.decode('UTF-8')


def getImg(html):
    # ------ 利用正则表达式匹配网页内容找到图片地址 ------
    reg = r'src="([.*\S]*\.jpg)"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

imgList = getImg(html)
imgName = 0
for imgPath in imgList:
    # ------ 这里最好使用异常处理及多线程编程方式 ------
    try:
        f = open('.\\tmp\pictures\\'+ str(imgName)+".jpg", 'wb')
        f.write((urllib.request.urlopen(imgPath)).read())
        print(imgPath)
        f.close()
    except Exception as e:
        print(imgPath+" error")
    imgName += 1

print("All Done!")


