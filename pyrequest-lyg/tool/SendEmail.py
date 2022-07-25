# encoding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import unittest
import time
import os.path



## ==============定义发送附件邮件==========
def send_file(file_new):
    msgRoot = MIMEMultipart('related')
    smtpserver = 'smtp.163.com'
    user = 'li1280208624@163.com'
    password = 'li123456789'
    sender = "li1280208624@163.com"
    receiver = 'xiwei@laoyuegou.com'

    # file = open(file_new, 'rb').read()

    basename = os.path.basename(file_new)

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    subject = '捞月狗' + now + '_result.html'
    att = MIMEText(open(file_new,'rb').read(),'html','utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename=%s" \
                                 % basename.encode('utf-8').decode('utf-8')

    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail('li1280208624@163.com', 'xiwei@laoyuegou.com',msgRoot.as_string())
    smtp.quit()


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序 win
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new