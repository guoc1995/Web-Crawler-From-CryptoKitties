# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

for i in range(0, 172):
    list = []
    for j in range(1, 10):
        page = j

        url = 'http://www.kittyexplorer.com/prices/?exclusive=&generation=' + str(i) + '&fancy=&color=&order=&page=' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }

        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            res_tr = r'<tr>(.*?)</tr>'
            m_tr = re.findall(res_tr, content, re.S|re.M);
            for line in m_tr:
                res_td = r'<td>(.*?)</td>';
                m_td = re.findall(res_td, line, re.S|re.M)
                for sline in m_td:
                    res_eth = r'(.*?) ETH';
                    m_eth = re.findall(res_eth, sline, re.S|re.M)
                    for line_eth in m_eth:
                        if len(line_eth):
                            list.append(line_eth)
            fileObject = open('gen' + str(i) +'_value.txt', 'w')
            for each in list:
                fileObject.write(each)
                fileObject.write('\n')
            fileObject.close()

        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason 









        