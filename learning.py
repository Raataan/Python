#!/usr/bin/env python
# -*- coding: utf-8 -*-
print '-------------------------------------------------------'
print '当前版本: 0.0.1 Beta'
name = raw_input('请告诉我你的名字：')
print name, '是猪头，哈哈，开玩笑。你好' + name
print '这是一个学习Python的笔记。'
while raw_input('继续[y/n]:') != 'y':
	print '已退出'
print '在print内容中若有\'或者\"请在前面打上\\'
print '一般变量取名为小写，常量为大写。Python是一个大小写敏感语言。'
print '你好，世界。', '想要在程序中使用中文，注意使用Unicode。'
while raw_input('继续[y/n]:') != 'y':
	print '已退出'
print '你好，%s' % name
print '上一行内容采用了格式化输出'
while raw_input('继续[y/n]:') != 'y':
	print '已退出'
user = [1,2,3]
user[0] = name
user[1] = raw_input('请输入性别：')
user[2] = int(raw_input('请输入年龄：'))
print '%s的个人信息：' % user[0]
print '性别：%s' % user[1]
print '年龄：%s' % user[2]
if user[2] < 18:
	print '抱歉，您未满18岁，不能学习Python，请自觉退出程序。'
elif user[2] > 60:
	print '抱歉，您年龄超过60岁，应该停止学习。'
else:
	print '您已通过年龄检测，欢迎！'
while raw_input('继续[y/n]:') != 'y':
	print '已退出'
print '接下来本程序将展示第一个功能，计算0-100的总和'
sum = 0
for i in range(101):
	sum += i
print '1+...+100 = ' + str(sum)
while raw_input('继续[y/n]:') != 'y':
	print '已退出'
print '提示：紧急情况下请立即退出程序'
dead = raw_input('请输入\'sb\'以获得100元奖励，不信试试:)')
if dead == 'sb':
	while 1 > 0:
		print '%s是傻逼' % user[0]
else:
	print '你应该为没有输入sb赶到庆幸，忘记这件事情吧！'
while raw_input('继续[y/n]:') != 'y':
	print '已退出'


