#!/usr/bin/env python
# coding: utf-8
import urllib
import re

from bs4 import BeautifulSoup
import re
url = 'http://www.heibanke.com/lesson/crawler_ex00/'
number = ['']

while True:
	html = urllib.urlopen(url + number[0])
	bs_obj = BeautifulSoup(html,"html.parser")
	numberstr = bs_obj.find("h3")
	numberstr = numberstr.get_text()
	number = re.findall(r'\d+', numberstr)
	print number[0]

