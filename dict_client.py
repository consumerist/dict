"""
dict_client.py
confiding:utf-8
电子字典客户端
"""
from socket import *
from multiprocessing import *
import getpass
import lock

# 全局变量
ADDR = "127.0.0.1"
PORT = 8888
ADDRESS = (PORT, ADDR)


def add_account(s):
    while True:
        name = input("User:")
        if not name:
            print("账号不能为空")
            continue
        break
    while True:
        password = getpass.getpass()
        if not password:
            print("密码不能为空")
            continue
        password1 = getpass.getpass("Again:")
        if password1 != password:
            print("两次密码不一样")
            continue
        break
    password = lock.lock(password, name)
    s.send(("A " + name + " " + password).encode())
    msg = s.recv(1024).decode()
    if msg == "OK":
        print("注册成功")
    else:
        print(msg.decode())
        print("注册失败")


def log(s):
    while True:
        name = input("user:")
        password = input("Password")
        s.send(("L " + name + " " + password).encode())
        date = s.recv(1024).decode()
        if date == "OK":
            print("登陆成功")
            index(s)
            return
        else:
            print("账号或密码错误,请重新输入")
            continue

def index(s):
    cmd = input("=======Query=======\n"
                "1.查单词 2.历史记录 3注销\n"
                "===================\n"
                "请输入操作命令:")
    if cmd == "1":
        search_word(s)
    elif cmd == "2":
        history(s)
    elif cmd == "3":
        return

def search_word(s):
    word = input("请输入查询单词/翻译:")
    s.send(("S " + word).encode())
    date = s.recv(1024)
    print(date.decode())

def history(s):
    pass
def main():
    # 搭建tcp网络模型
    s = socket()
    s.connect((ADDR, PORT))
    while True:
        cmd = input("-------Welcome------\n"
                    "  1.注册 2.登录 3.退出\n"
                    "--------------------\n"
                    "请输入操作：")
        if cmd == "1":
            add_account(s)
        elif cmd == '2':
            log(s)
        elif cmd == '3':
            s.send("Q".encode())
            s.close()
            break


if __name__ == "__main__":
    main()
