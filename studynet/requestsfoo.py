#  requests库的使用
import requests
# response = requests.get("http://www.baidu.com")
# print(type(response))
# print(type(response.text))
# print(response.text)
# print(response.content)
# print(response.cookies)
# print(response.content.decode("utf8"))
# data = {
#     'name':'zhangsan',
#     'age':12
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.url)
# print(response.text)
# response = requests.get("http://www.zhihu.com")
# print(response.text)
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# response = requests.get('https://www.zhihu.com',headers=headers)
# print(response.text)
response = requests.get('http://www.baidu.com')
print (response.cookies)
for k,v in response.cookies.items():
    print (k+'='+v)