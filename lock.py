"""
lock.py
加密
"""
import hashlib
def lock(pwd,user,salt="#abc"):
    password = user + salt + pwd
    answer = hashlib.sha256()
    answer.update(password.encode())
    return answer.hexdigest()