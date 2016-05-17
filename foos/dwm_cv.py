# /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import re


def color(messages):
    color = "\x1B[%d;%dm" % (1, random.randint(30, 37))
    return "%s %s\x1B[0m" % (color, messages)


def colorprint(mes, flag=True):
    def _mydecorator(func):
        def _mydecorator(*args):
            res = func(*args)
            print
            color(mes + ":"), "\n"
            if flag:
                for k1, v1 in res.items():
                    if not isinstance(v1, dict):
                        print
                        "{0}: {1}".format(k1.rjust(16), v1)
                    else:
                        print
                        "{0}:".format(k1.rjust(16))
                        for k2, v2 in v1.items():
                            print
                            "{0}: {1}".format(k2.rjust(20), v2)
            else:
                for i in res:
                    if not isinstance(i[1], dict):
                        print
                        i
                    else:
                        for k, v in i[1].items():
                            print
                            "{0}[{1}]: {2}".format(k.rjust(16), \
                                                   i[0], v)
            return res

        return _mydecorator

    return _mydecorator


class ForJob(object):
    def __str__(self):
        return color("XXX的python简历".center(400))

    @property
    @colorprint("个人信息")
    def personal_information(self):
        return {
            "Name": "XXX",
            "Gender": "Male",
            "Born": ['19XX', 'X', 'X'],
            "Education": {
                "School Name": "保定科技职业学院",
                "Major": "烹饪工艺与营养",
                "Degree": "Three-year college",
                "Graduation": 2009},
            "QQ": 61966225,
            "Tel": 13552651322,
            "Email": "ciici1234@hotmail.com",
            "Target Positions": re.compile("'Python Developer'|Architect|DevOps", re.I | re.M).pattern}

    @property
    @colorprint("个人特点")
    def characteristics(self):
        return {
            "心里承受能力强": "从非计算机专业―思科方向\
―linux运维―C/python开发",
            "对计算机技术的热衷和喜爱": "正是因为喜欢IT,\
我才会放弃大学专业",
            "自学能力强": "没有大学的计算机基础除思科参加培训，\
其它都为都是自学",
            "毅力和耐性": "从不放弃一个解决不了的难题，\
看过的计算机专业技术多于700页的书籍>30本",
            "is_geek": True}

    @property
    @colorprint("个人能力")
    def skills(self):
        return {
            "Language": {
                "熟悉": ["Python", "Ruby", "Bash", "c"],
                "了解": ["Haskell", "Lisp", "Erlang"]},
            "OS": ["Gentoo", "Debian", "Centos/Rhel", "Opensuse"],
            "Tool": ["Vim", "Mercurial", "Git"],
            "Databaseandtools": ["Mysql",
                                 "Postgresql", "Mongodb", "Redis", "Memcached", "Sqlalchemy"],
            "WebFramework": {
                "熟悉": ["Tornado", "Django", "Gae"],
                "了解": ["Flask"]},
            "OtherFramework": ["Twisted", "gevent",
                               "stackless", "scrapy", "mechanize"],
            "GUI": "pyqt",
            "Network": "Cisco Certified Security Professional",
            "Other": "给gentoo和centos提交过bug"}

    @property
    @colorprint("工作经验", False)
    def work_experience(self):
        return enumerate([
            {
                "Time period": "2009.09-2011.08",
                "Company Name": "XXX（北京）科技股份有限公司",
                "Position": "高级运维工程师"},
            {
                "Time period": "2011.09-2012.08",
                "Company Name": "北京XXX有限责任公司",
                "Position": "linux python研发工程师"}])

    @property
    @colorprint("项目经验", False)
    def project_experience(self):
        return enumerate([
            {
                "Project": "kvm远程管理系统",
                "Description": "前台(django)接手至其它同事并完成维护，\
后台独立完成，用来创建，修改，删除kvm，查看状态信息等"},
            {
                "Project": "postfix群发邮件系统",
                "Description": "前台(tornado),为其它部门提供发送邮件的web端, \
并作为数据收集服务端,前后台独立完成"},
            {
                "Project": "windows个人安全终端系统",
                "Description": "前后台和接收数据的socket服务器独立完成，\
客户端图形编程使用qt"},
            {
                "Project": "地推(一个分布在全国的各个办事处的称呼:地面推广) \
IDC质量测试系统",
                "Description": "还在代码实现中,前台flask, \
数据接收服务准备使用twisted,客户端为windows进程"}])

    @property
    @colorprint("@Where", False)
    def findme(self):
        return enumerate([
            {
                "Link": "http://www.dongwm.com",
                "Description": "个人技术博客"},
            {
                "Link": "http://www.zhihu.com/people/dongweiming",
                "Description": "知乎"},
            {
                "Link": "http://www.quora.com/Weiming-Dong",
                "Description": "Quora"},
            {
                "Link": r"https://twitter.com/#!/dongweiming",
                "Description": "Twitter"},
            {
                "Link": "http://www.ailll.com",
                "Description": "音乐分享网站"},
            {
                "Link": "http://dongwm.blog.51cto.com",
                "Description": "51cto的推荐博客"},
            {
                "Link": "http://youhouer.appspot.com",
                "Description": "基于Google App Engine的前端网站"}])

    def show(self):
        prolist = [i for i in dir(self) if not i.startswith("_") \
                   and not i.startswith("personal")]
        self.personal_information
        for pro in prolist:
            getattr(self, pro)


if __name__ == "__main__":
    dongweiming = ForJob()
    print
    dongweiming
    dongweiming.show()
