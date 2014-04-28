#coding:utf-8
import time
import os
import hashlib
import random
'''
	日志标准类
	使用:
		import 目录名.Logmark_Class
		obj=Logmark_Class(输出方式)
		obj.log_do(日志内容,是否设置个性文件名)
'''
class Logmark_Class(object):
	'''
		初始化设置参数
		log_mode:
			1、print
			2、save
	'''
	def __init__(self,log_type=1):
		self.log_type=log_type
		m=hashlib.md5(str(random.randint(1,100000))+"SmartLog")
		self.m_hash=m.hexdigest()
	'''
		日志目录检测，日志写入
	'''
	def save_log(self,file_name,log_text):
		if os.path.isdir("log_filter"):
			file_object=open("log_filter/"+file_name,'a')
			try:
				file_object.write(log_text+"\n")
			finally:
				file_object.close()
		else:
			try:
				os.mkdir("log_filter")
				file_object=open("log_filter/"+file_name,'a')
				file_object.write(log_text+"\n")
			finally:
				file_object.close()		
	'''
		日志操作判断
	'''
	def log_do(self,log,last_name=None):
		static_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		filename_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
		if self.log_type==1:
			print "[*][%s] %s" % (static_time,log)
		elif self.log_type==2:
			log_text="[*][%s] %s" % (static_time,log)
			if last_name!=None:
				file_name=filename_time+'-'+last_name+".log"
				self.save_log(file_name,log_text)
			else:
				file_name=filename_time+"-"+self.m_hash[0:5]+".log"
				self.save_log(file_name,log_text)
		else:
			print "Nothing to do!!!"

# if __name__=='__main__':
# 	obj=Logmark_Class(2)
# 	for i in range(10):
# 		obj.log_do("FUCK!!!")
# 		time.sleep(2)