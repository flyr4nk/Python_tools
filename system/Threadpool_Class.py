#coding:utf-8
'''
   多线程标准类
   使用：
    	import 目录名.Threadpool_Class
    	obj=Threadpool_Class.Threadpool_Class(线程最大数)
    	for 数据参数 in 列表:
    		obj.add_pool(数据参数)
    	obj.exec_pool(程序函数)
'''
import threading
import Queue
import time

class Threadpool_Class(object):

	'''
		1、建立空的队列
		2、设置可并行的线程数量
	'''
	def __init__(self,thread_sum=5):
		self.queue=Queue.Queue()
		self.thread_sum=thread_sum
		self.threads_list=[]

	'''
		将任务添加到队列中
	'''
	def add_pool(self,task):
		# 把任务放入队列
		self.queue.put(task)

	'''
		取出队列任务并且启动线程
	'''
	def exec_pool(self,func):
		while True:
			if self.queue.empty():
				print "Finish Work!"
				break
			else:
				# 创建线程使用
				for i in range(self.thread_sum):
					task=self.queue.get()
					thr=threading.Thread(target=func,args=(task,))
					self.threads_list.append(thr)
					thr.start()

				for item in self.threads_list:
					if item.isAlive():
						item.join()
						self.threads_list.remove(item)

# if __name__=='__main__':
# 	t=PoolClass(10)
# 	for i in range(100):
# 		t.add_pool(i)
# 	t.exec_pool(jobtest)
