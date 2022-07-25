# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from tool import SendEmail
from db_fixture import test_data
import time
import os
import sys
import io
sys.path.append('./db_fixture')
sys.path.append('./interface')
sys.path.append('./report')
from unittest import defaultTestLoader


# 用例目录
test_dir = './interface'
# 报告目录
Report_dir = './report'
#testsuit = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据

    testsuit = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = Report_dir
    filename = './report/' + now + '_result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='LYG接口自动化测试',
        description='运行环境：MySQL(PyMySQL),Requests,unittest'
    )

    runner.run(testsuit)
    fp.close()
    new_report = SendEmail.new_report(test_report)
    SendEmail.send_file(new_report)

