from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "Tarena")

#　主线程退出分支线程也退出
t.setDaemon(True)

t.start()

#　线程名称
t.setName("Tedu")
print("Thread name:",t.getName())

# 线程生命周期
print("is alive:",t.is_alive())



