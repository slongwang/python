#!/usr/bin/python
# coding=utf-8
import urllib2
import re
import time
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )
f = open('a.txt', "w+")
class Sub:
    replaceBr = re.compile('<br/>')
    replaceB = re.compile('</*span>')
    def replace(self,x):
        x = re.sub(self.replaceBr,"\n",x)
        x = re.sub(self.replaceB, " ", x)
        return x.strip()

class spiderMode:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False
        self.sub = Sub()


    def getPage(self,page):
        sUrl = "http://www.qiushibaike.com/8hr/page/"+page
        userAgent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent': userAgent}
        request = urllib2.Request(sUrl, headers=headers)
        response = urllib2.urlopen(request)
        sPage = response.read()
        unicodePage = sPage.decode("utf-8")
        myItems = re.findall('<div class="content">(.*?)</div>',unicodePage,re.S)
        num = 1
        for item in myItems:
            xh = str(num) + '. ' + self.sub.replace(item)
            print xh + '\n'
            f.write(xh + '\n')
            f.flush()
            num += 1
            time.sleep(0.5)
        return None
    def loadPage(self):
        for i in range(1, 11):
            f.write("--------------------------------"+'\n')
            print r'pages:%d' % i
            mypage = self.getPage(str(i))
            i += 1
            self.pages.append(mypage)
            time.sleep(2)
        f.close()
model =spiderMode()
model.loadPage()
# http://www.qiushibaike.com/8hr/page/3/