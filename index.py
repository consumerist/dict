import getpass
import hashlib

pwd = getpass.getpass()
hah = hashlib.sha256()
hah.update(pwd.encode())
pwd = hah.hexdigest()
print(pwd)
