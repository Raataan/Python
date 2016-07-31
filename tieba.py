#!/usr/bin/env python
# coding: utf-8
#07/31/2016

'tieba'

__author__ = 'Yuetao Li'

import requests
import re


#————————————————————————————————————————————————————————————————

#此函数用于获取帖子的全部代码
def getPage(url):
    r = requests.get(url)
    return r.text
    #print r.text 测试函数


#此函数用于获取帖子的标题
def getTitle(url):
    page = getPage(url) #使用getPage函数获得帖子的代码
    pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S) #规定正则表达试的pattern
    title = re.search(pattern, page) #使用正则表达式在page中进行搜索
    print title.group(1) #.group(1)代表第一个正则表达的匹配
#getTitle(tieba)测试获取标题


#此函数用于获取帖子的正文内容
def getContent(url):
    page = getPage(url) #使用getPage函数获得帖子的代码
    pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S) #规定正则表达试的pattern
    contents = re.findall(pattern, page) #因为有多个内容所以使用findall,标题只有一个所以使用search
    floor = 1
    for content in contents:
        print floor, u"楼"
        print "------------------------------------------------------------------------"
        print prettify(content)
        print "\n"
        floor += 1

#此函数用于美化帖子排版
def prettify(x):
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    x = re.sub(removeImg, "", x)
    x = re.sub(removeAddr, "", x)
    x = re.sub(replaceLine, "\n", x)
    x = re.sub(replaceTD, "\t", x)
    x = re.sub(replacePara, "\n    ", x)
    x = re.sub(replaceBR, "\n", x)
    x = re.sub(removeExtraTag, "", x)
    x = x.strip() #.strip()用于去掉多余内容
    return x

#————————————————————————————————————————————————————————————————
tieba = raw_input('请输入帖子地址：')
getContent(tieba)

