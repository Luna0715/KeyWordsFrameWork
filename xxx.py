#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import urllib #http
import urllib.request
import re #导入正则

def load_photo(url):
    rq=urllib.request.Request(url) #请求网址
    rp=urllib.request.urlopen(rq) #等待响应
    data=rp.read() #获取返回结果
    return data
def get_photo(html):
    regx=r"http://[\S]*png" #存储正则表达式
    pattern=re.compile(regx)
    get_image=re.findall(pattern,repr(html))
    num=1
    for img in get_image:
        imgs=load_photo(img)
        with open (r"E:\test_test_test\test_thing\%s.png" %num,"wb")as f:
            f.write(imgs)
            print("正在下载%s张图片" %num)
            num=num+1
print("下载完成!")
#url = "http://p.weather.com.cn/2019/09/3239162.shtml"  # 爬取的网页
url = "http://p.weather.com.cn/2017/06/2720826.shtml#p=7"  # 爬取的网页
html = load_photo(url)
get_photo(html)