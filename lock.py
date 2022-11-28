"""
lock.py
加密
"""
import hashlib
import operation
def lock(pwd,user,salt="#abc"):
    password = user + salt + pwd
    answer = hashlib.md5()
    answer.update(password.encode())
    return answer.hexdigest()


