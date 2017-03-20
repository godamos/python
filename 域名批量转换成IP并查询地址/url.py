#encoding=utf-8
import urllib2
import requests
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

ff=open('quadgrams.txt','r')
result=ff.readlines()
for ceshi in result:
	try:
		url=r"http://ip.chinaz.com/ajaxsync.aspx?at=ipbatch&callback=jQuery111306097377031110227_1489638697154"
		value={"ip":ceshi}
		data=urllib.urlencode(value)
		r=urllib2.Request(url,data)
		reponse=urllib2.urlopen(r)
		html=reponse.read()
		print html
		domain = re.search(r'domain:\'(.*?)\',', html)
		#print domain
		location=re.search(ur"[\u4e00-\u9fa5 ]+",html.decode('utf8'))
		#print location.group()
		fin=domain.group(1)+':'+location.group()
		f=open('result.txt','a+')
		f.write(fin+'\n')
		f.close
	except:
		pass


