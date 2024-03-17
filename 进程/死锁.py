import threading

# 创建互斥锁
lock = threading.Lock()


def get_value(index):
    # 上锁
    lock.acquire()
    my_list = [1, 4, 6]
    if index >= len(my_list):
        print("下标越界：", index)
        lock.release()
    value = my_list[index]
    print(value)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建子线程
    for i in range(10):
        t = threading.Thread(target=get_value, args=(i,))
        t.start()
    # 启动线程
