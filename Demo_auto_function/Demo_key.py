#-*- coding:utf-8 -*-

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()


import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()
def calc_md5(password):
    return get_md5(password + 'the-Salt')
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
def get_md5(mingwen):
    sha1.update(mingwen)