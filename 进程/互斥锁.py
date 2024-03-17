import threading

g_num = 0

# 创建互斥锁
lock=threading.Lock()

def task1():
    # 上锁
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num = g_num + 1
    print("task1:", g_num)
    # 释放锁
    lock.release()



def task2():
    # 上锁
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num = g_num + 1
    print("task2:", g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建子线程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    # 启动线程
    first_thread.start()
    second_thread.start()
