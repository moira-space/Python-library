# 导入进程包
import multiprocessing

def Fun():
    for i in range(3):
        print(1)
#创建子进程
a=multiprocessing.Process(target=Fun)
# 启动子进程
a.start()
