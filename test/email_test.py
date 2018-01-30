# coding:utf-8

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '*****@163.com'
password = '*****'
to_addr = '*****@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('Python exception, HTTP 403', 'plain', 'utf-8')
msg['From'] = from_addr #_format_addr('First Spider<%s>' % from_addr)
msg['To'] = to_addr# _format_addr('Admin<%s>' % to_addr)
msg['Subject'] = Header('First Spider state', 'utf-8').encode()

#server = smtplib.SMTP(smtp_server, 25)
server = smtplib.SMTP()
server.connect(smtp_server)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()