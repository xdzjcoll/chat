from multiprocessing import Process
import os
from time import sleep

filename = "./timg.jpeg"
#　获取图片大小
size = os.path.getsize(filename)

#　父进程打开文件
#　文件偏移量会相互影响
# f = open(filename,'rb')

#　复制上半部分
def top():
    sleep(1)
    f = open(filename,'rb')
    n = size // 2
    fw = open("top.jpeg",'wb')
    fw.write(f.read(n))
    f.close()
    fw.close()

#　下半部分
def bot():
    f = open(filename,'rb')
    fw = open('bot.jpeg','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

t = Process(target=top)
b = Process(target=bot)
t.start()
b.start()
t.join()
b.join()

