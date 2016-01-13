#-*- coding:utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle
d=dict(name="zhangsan",age=20,scorc=88)
pickle.dumps(d)
f = open('myapp.log', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
