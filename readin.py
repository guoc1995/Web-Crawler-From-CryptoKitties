# -*- coding: utf-8 -*- 
import xlwt
import urllib
import urllib2
import re

def testXlwt(file = 'gen_value.xls'):
    book = xlwt.Workbook()
    sheet = book.add_sheet('new') 
    col = -1
    for i in range(0, 172):
    	col = col + 1
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
	            row = 0
	            for each in list:
	            	try:
	            		sheet.write(row, col, each)
	            	except:
	            		sheet._cell_overwrite_ok = True
	            		sheet.write(row, col, "new text")
	            		sheet._cell_overwrite_ok = False
	                row = row + 1

	        except urllib2.URLError, e:
	            if hasattr(e,"code"):
	                print e.code
	            if hasattr(e,"reason"):
	                print e.reason 

    book.save(file)

# main function
def main():
   testXlwt()

if __name__=="__main__":
    main()







