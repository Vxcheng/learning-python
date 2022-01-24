import _thread
import time


def print_time( thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (thread_name, time.ctime(time.time())))


try:
    _thread.start_new_thread(print_time, ("thread-1", 1,))
    _thread.start_new_thread(print_time, ("thread-2", 2,))
finally:
     print ("线程开启")
# else:
#    print ("Error: 无法启动线程")


'''
使用 threading 模块创建线程
'''

import threading
import time

exitFlag = 0

class MyThread(threading.Thread):
    """
    docstring
    """
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter
    
    def run(self):
        """
        docstring
        """
        print ("开始线程：" + self.name)
        threading_print_time(self.name, self.counter, 1)
        print ("退出线程：" + self.name)


def threading_print_time(name, counter, delay):
    """
    docstring
    """
    while counter:
        if exitFlag:
            name.exit()
        
        time.sleep(delay)
        print ("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
exitFlag = 1
print ("退出主线程threading")


# 线程优先级队列（ Queue）
import queue
import threading
import time

exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            print ("%s processing %s" % (threadName, data))

        queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)

threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for name in nameList:
    workQueue.put(name)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
