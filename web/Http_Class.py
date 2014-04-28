#coding:utf-8
import urllib2,urllib,cookielib
'''
	Http标准请求类
	使用:
		obj=Http_Class()
		obj.__main("get","http://www.baidu.com")
		obj.__main("get","http://www.baidu.com","代理IP")
		obj.__main("post","http://www.baidu.com","{'username':'admin','password':'admin'}")
		obj.__main("post","http://www.baidu.com","{'username':'admin','password':'admin'}","代理IP")
	返回:
		HTML结果
'''
class Http_Class(object):
	'''
		初始化设置参数
	'''
	def __init__(self,timeout=5,cookies=False):
		self.timeout=timeout
		self.cookies=cookies

	'''
		GET 方法请求
		1、url地址
		2、代理IP
	'''
	def _get(self,url,proxy_ip=None):
		if proxy_ip:
			proxy_support = urllib2.ProxyHandler(proxy_ip)
			opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
			urllib2.install_opener(opener)
			request = urllib2.Request(url)
			return urllib2.urlopen(request,timeout=self.timeout).read()
		else:
			return urllib2.urlopen(url,timeout=self.timeout).read()

	'''
		POST 方法请求
		1、url地址
		2、提交内容
		3、代理IP
	'''
	def _post(self,url,postbody,proxy_ip=None):
		data=urllib.urlencode(postbody)
		req=urllib2.Request(url)
		cookiejar = cookielib.CookieJar()
		if proxy_ip:
			proxy_support=urllib2.ProxyHandler(proxy_ip)
			if self.cookies:
				cokes=cookielib.CookieJar();
				opener=urllib2.build_opener(proxy_support,urllib2.HTTPHandler,urllib2.HTTPCookieProcessor(cokes))
			else:
				opener=urllib2.build_opener(proxy_support,urllib2.HTTPHandler,urllib2.HTTPCookieProcessor())
			urllib2.install_opener(opener)
			return opener.open(req,data).read()
		else:
			if self.cookies:
				cokes=cookielib.CookieJar();
				opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cokes))
			else:
				opener=urllib2.build_opener(urllib2.HTTPCookieProcessor())
			return opener.open(req,data).read()
		
	'''
		判断使用什么样的请求
		主体控制
	'''
	def __main(self,method,url,data=None,Proxy_ip=None):
		if method=="get":
			if Proxy_ip:
				self._get(url,Proxy_ip)
			else:
				self._get(url)
		elif method=="post":
			if data:
				if Proxy_ip:
					self._post(url,data,Proxy_ip)
				else:
					self._post(url,data)
			else:
				print "[*] Data mustn't NUll!"
		else:
			print "[*] Nothing to do!"

# if __name__=='__main__':
	# obj=Http_Class()
	# print obj._get("http://www.baidu.com/")