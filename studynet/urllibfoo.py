#  ============================1.简单的请求
# import urllib.request
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))
# ==============================2.捕捉异常 + post请求
# import urllib.parse
# import urllib.request
# import socket
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# try :
#     response = urllib.request.urlopen("http://httpbin.org/post",data,timeout=0.1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     if(isinstance(e.reason,socket.timeout)):
#         print("超时")
# ==========================3.返回码
# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))
# =========================4.带头部的url请求
# from urllib import request,parse
# dictdata = {
#     "hello" : "world"
# }
# url = 'http://httpbin.org/post'
# header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# data = bytes(parse.urlencode(dictdata),encoding="utf8")
# req = request.Request(url=url,headers=header,data=data,method="POST")
# reponse = request.urlopen(req)
# print(reponse.read().decode("utf-8"))
# =======================5.设置代理
# from urllib import request,parse
# proxy_handler = request.ProxyHandler(
#     {
#         'http': 'http://127.0.0.1:8087',
#         'https': 'https://127.0.0.1:8087'
#     }
# )
# opener = request.build_opener(proxy_handler)
# response = opener.open("http://httpbin.org/get")
# print(response.read())
# ======================异常捕捉
from urllib import request,error
try:
    response = request.urlopen("http://pythonsite.com/1111.html")
    print(response.read().decode("utf-8"))
except error.HTTPError:
    print("URL错误")