# -*- coding: utf-8 -*-
'''
Author: Fantasy
Date: 2020-11-03 19:22:24
LastEditors  : Please set LastEditors
LastEditTime : 2022-04-10 21:09:24
Descripttion: 
Email: 776474961@qq.com
'''

import httpx
import re
from lxml import etree


class Report(object):
    """
    微信上报
    """
    def __init__(self, username, password, name="anonymous"):
        self.username = username
        self.password = password
        self.printInfo = name + ':' + username
        self.login_url = 'http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do'
        self.apply_url = 'http://yiqing.ctgu.edu.cn/wx/health/toApply.do'
        self.save_url = 'http://yiqing.ctgu.edu.cn/wx/health/saveApply.do'
        self.logout_url = 'http://yiqing.ctgu.edu.cn/wx/index/logout.do'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
        }
        self.login_count = 0
        self.session = httpx.Client(headers=self.headers, timeout=30)

    def login(self):
        """
        登陆
        """
        self.login_count += 1
        login_data = {'username': self.username, 'password': self.password}
        resp = self.session.post(self.login_url, data=login_data)
        if 'success' == resp.text:
            print("用户 {} 第 {} 次登陆成功".format(self.printInfo, self.login_count))
            return True
        elif 'fail' == resp.text:
            print("用户 {} 密码错误，请检查配置文件".format(self.printInfo))
            return False
        elif self.login_count < 3:
            print("用户 {} 第 {} 次登陆失败，正在重试".format(self.printInfo, self.login_count))
            return self.login()
        else:
            print("用户 {} 第 {} 次登陆失败，超过重试次数，请检查系统...".format(self.printInfo, self.login_count))
            print(resp.text)
            return False

    def apply_info_extract(self):
        """
        上报信息提取
        """
        resp = self.session.get(self.apply_url)
        if re.findall(r'提交', resp.text):
            report_data = {}
            resp_html = etree.HTML(resp.text)
            all_input = resp_html.xpath('//input')
            for input_t in all_input:
                input_name = input_t.get('name')
                input_value = input_t.get('value')
                if input_name != None and len(input_name) > 0:
                    report_data[input_name] = input_value
            return report_data
        else:
            print("用户 {} 今日已上报过".format(self.printInfo))
            return False

    def send_report(self):
        """
        发起上报
        """
        report_data = self.apply_info_extract()
        if report_data:
            resp = self.session.post(self.save_url, data=report_data)
            if re.findall(r'true', resp.text):
                print("用户 {} 上报成功".format(self.printInfo))
            else:
                print("用户 {} 上报失败：".format(self.printInfo))
                print(resp.text)

    def logout(self):
        """
        注销
        """
        resp = self.session.get(self.logout_url)
        if re.findall(r'请输入用户名', resp.text):
            print("用户 {} 注销成功".format(self.printInfo))
        else:
            print("用户 {} 注销失败：".format(self.printInfo))
            print(resp.text)
        self.session.close()

    def run(self):
        """
        上报流程
        """
        if self.login():
            self.send_report()
            self.logout()