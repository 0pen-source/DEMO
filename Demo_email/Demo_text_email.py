#-*- coding:utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令:
# from_addr = raw_input('From: ')
from_addr="zhaochenxiao90@126.com"
# password = raw_input('Password: ')
password="0304@siqilove"
# 输入SMTP服务器地址:
# smtp_server = raw_input('SMTP server: ')
smtp_server="smtp.126.com"
# 输入收件人地址:
# to_addr = raw_input('To: ')
to_addr="zhaochenxiao@hichao.com"
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

