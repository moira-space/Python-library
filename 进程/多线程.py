import threading
import time


def task():
    print("---------")

if __name__ == '__main__':
    # daemon=True表示创建的子线程守护主线程，主线程退出子线程直接销毁
    # sub_thread = threading.Thread(target=task,daemon=True)
    sub_thread = threading.Thread(target=task)
    # 表示创建的子线程守护主线程，主线程退出子线程直接销毁
    sub_thread.setDaemon(True)
    sub_thread.start()
    # 主线程延时1秒
    time.sleep(1)
    print("结束")
