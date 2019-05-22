from threading import Thread


class ThreadClass(Thread):
    def __init__(self, attr):
        self.attr = attr
        super().__init__()

    # 多个方法配合实现具体功能
    def f1(self):
        print("步骤１",self.attr)

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()

t = ThreadClass("xxxxx")
t.start()  #　自动运行ｒｕｎ方法
t.join()