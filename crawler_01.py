# -*- coding: utf-8 -*-
# CopyRight by heibanke
import requests

url = '202.96.165.8/EI/Login.aspx?ReturnUrl=%2fEI%2f'
form = {'TxtUserName': '2014530432', 'TxtPassword': '98055'}
r = requests.post(url, data = form)
print r.text	