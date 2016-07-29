# -*- coding: utf-8 -*-
# CopyRight by heibanke
import requests

url = 'http://202.96.165.8/EI/Login.aspx'
form1 = {'TxtUserName': '2014530432', 'TxtPassword': '19255'}
h = { 		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Referer":"http://www.example.com/",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Referer":"http://202.96.165.8/EI/Login.aspx?ReturnUrl=%2fEI%2f"}
r = requests.post(url,data = form1,headers = h)
print r.text