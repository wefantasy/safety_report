# -*- coding: utf-8 -*- 
'''
Author: Fantasy
Date: 2020-11-03 20:32:46
LastEditors  : Please set LastEditors
LastEditTime : 2022-04-10 21:09:31
Descripttion: 
Email: 776474961@qq.com
'''
from safety_report.report import Report
from safety_report import setting

if __name__ == "__main__":
    for account in setting.ACCOUNTS:
        report = Report(account[0], account[1], account[2])
        report.run()