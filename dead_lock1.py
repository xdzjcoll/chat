from threading import Thread,RLock
import time

num = 0 #　共享资源
lock = RLock()  #　在一个线程内可以对锁进行重复加锁

class MyThread(Thread):
    def fun1(self):
        global num
        with lock:   #　上锁
            num -= 1

    def fun2(self):
        global num
        time.sleep(2)
        if lock.acquire():
            num += 1
            print(self.name,"set Num = ",num)
            self.fun1()
            lock.release()

    def run(self):
        self.fun2()

for i in range(10):
    t = MyThread()
    t.start()

