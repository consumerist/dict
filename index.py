# import getpass
# import hashlib
#
# pwd = getpass.getpass()
# hah = hashlib.sha256()
# hah.update(pwd.encode())
# pwd = hah.hexdigest()
# print(pwd)
if __name__=="__main__":
    while True:
        choice = input("-----------------\n"
                       "--  欢迎您的到来 --\n"
                       " 1.注册   2.登录  \n"
                       "-----------------\n"
                       "请输入您地操作项：")
        if choice == "1":
            
