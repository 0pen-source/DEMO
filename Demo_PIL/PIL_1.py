#-*- coding:utf-8 -*-
# 在Debian/Ubuntu Linux下直接通过apt安装：
#
# $ sudo apt-get install python-imaging
#
# Mac和其他版本的Linux可以直接使用easy_install或pip安装，安装前需要把编译环境装好：
#
# $ sudo easy_install PIL
import Image
im=Image.open("/home/chenxiao/Pictures/123.jpg")
w,h =im.size
print(w,h)
# im.thumbnail((w//2, h//2))
im.save('/home/chenxiao/Pictures/1233.jpg','jpg')
