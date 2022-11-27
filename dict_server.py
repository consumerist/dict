"""
dict_client.py
confiding:utf-8
电子字典客户端
模型：多进程 tcp并发
"""
from socket import *

# 全局变量
ADDR = "127.0.0.1"
PORT = 8888
ADDRESS = (PORT,ADDR)

# 搭建tcp网络模型
s = socket()
s.bind(ADDRESS)
s.listen(3)
print("")
while True:
