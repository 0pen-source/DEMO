#-*- coding:utf-8 -*-
# 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
#
# [client]
# default-character-set = utf8
#
# [mysqld]
# default-storage-engine = INNODB
# character-set-server = utf8
# collation-server = utf8_general_ci


# 检查文字编码
# show variables like '%char%';


# 目前，有两个MySQL驱动：
#
#     mysql-connector-python：是MySQL官方的纯Python驱动；
#
#     MySQL-python：是封装了MySQL C驱动的Python驱动。
#
# 可以把两个都装上，使用的时候再决定用哪个：
#
# $ easy_install mysql-connector-python
# $ easy_install MySQL-python

# 导入MySQL驱动:
import MySQLdb
# 注意把password设为你的root口令:
conn=MySQLdb.connect(host="localhost",user="root",passwd="0304siqi",db="wodfan",charset="utf8")
cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Michael'])
cursor.rowcount
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', '1')
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()

