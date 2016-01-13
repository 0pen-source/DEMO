#-*- coding:utf-8 -*-
import os
import codecs
# with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
#     f.read() # u'\u6d4b\u8bd5'
# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')


[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']