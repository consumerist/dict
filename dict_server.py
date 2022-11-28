"""
dict_client.py
confiding:utf-8
电子字典客户端
模型：多进程 tcp并发
"""
import sys
from socket import *
from multiprocessing import *
from signal import *

import lock
from operation import *

# 全局变量
ADDR = "127.0.0.1"
PORT = 8888
ADDRESS = (PORT, ADDR)
db = Database("dict")
db.Connect()
db.Cursor()


def add_account(cmd, config):
    name = cmd[1]
    password = cmd[2]
    # 返回值True则注册成功
    if db.Search(name, password):
        config.send(b"OK")
    else:
        config.send("用户名已存在".encode())


def log(cmd, config):
    name = cmd[1]
    password = cmd[2]
    password = lock.lock(password, name)
    result = db.log(name, password)
    if result:
        config.send(b"OK")
    else:
        config.send("账号或密码错误")


def search_word(cmd, config):
    word = cmd[1]
    word_list = " ".join(db.Search_word(word))
    if word_list:
        config.send(word_list.encode())
    else:
        config.send("该单词不存在".encode())


# 接收客户端请求，分配处理函数
def request(config):
    while True:
        date = config.recv(1024)
        cmd = date.decode().split(" ")
        if not date or cmd[0] == "Q":
            config.close()
            break
        elif cmd[0] == 'A':
            add_account(cmd, config)
        elif cmd[0] == "L":
            log(cmd, config)
        elif cmd[0] == "S":
            search_word(cmd, config)


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((ADDR, PORT))
    s.listen(3)
    # signal(SIGCHLD, SIG_IGN)
    print("connect to port 8888")
    while True:
        try:
            config, addr = s.accept()
            print("come from ", addr)
        except KeyboardInterrupt:
            db.close()
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        # 为客户端创建进程
        p = Process(target=request, args=(config,))
        # 父进程结束子进程结束
        p.daemon = True
        p.start()
        p.join()


# 搭建tcp网络模型
if __name__ == "__main__":
    main()
