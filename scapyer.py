import urllib
url = 'http://webcrawler.cookdata.cn/httpbin/get'

# 请在下方作答 #

response1 = urllib.request.urlopen(url, timeout=2)
content1 = response1.read()

request = urllib.request.Request(url)
response2 = urllib.request.urlopen(request, timeout=2)
content2 = response2.read()

print(content1 == content2)



import urllib
import json
url_get = 'http://webcrawler.cookdata.cn/httpbin/get'
url_post = 'http://webcrawler.cookdata.cn/httpbin/post'

# 请在下方作答 #
kvs = 'k1=v1&k2=v2'

content = urllib.request.urlopen(url_get + '?' + kvs, timeout=5).read()
args = json.loads(content)['args']

content = urllib.request.urlopen(url_post, data=kvs.encode("utf-8"), timeout=5).read()
form = json.loads(content)['form']

print(args == form)




    1 	import urllib
    2 	import json
    3 	url = 'http://webcrawler.cookdata.cn/httpbin/headers'
    4 	request = urllib.request.Request(url)
    5 	
    6 	User_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    7 	Referer = 'http://webcrawler.cookdata.cn'
    8 	Host = 'webcrawler.cookdata.cn'
    9 	Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
   10 	Accept_Encoding  =  'gzip, deflate'
   11 	
   12 	# 请在下方作答 #
   13 	
   14 	request.add_header('User-Agent',User_agent)
   15 	request.add_header('Referer',Referer)
   16 	request.add_header('Host',Host)
   17 	request.add_header('Accept',Accept)
   18 	request.add_header('Accept-Encoding',Accept_Encoding)
   19 	
   20 	content=urllib.request.urlopen(request,timeout=5).read()
   21 	headers_from_response=json.loads(content)['headers']
