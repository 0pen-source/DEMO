#-*- coding:utf-8 -*-
# deque
#
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print q[2]
# print q


# Python内置的base64可以直接进行base64的编解码：

import base64
base64.b64encode('binary\x00string')
base64.b64decode('YmluYXJ5AHN0cmluZw==')

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

base64.b64encode('i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
base64.urlsafe_b64decode('abcd--__')


