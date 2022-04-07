# import os, binascii
# from backports.pbkdf2 import pbkdf2_hmac

# salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
# passwd = input('password: ').encode("utf8")
# key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
# print("Salt:", salt)
# print("Derived key:", binascii.hexlify(key))

#HMAC Code example
# import hashlib, binascii
# dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
# print(hashlib.algorithms_available)
# print (dk)
# binascii.hexlify(dk)

# salt = binascii.unhexlify(binascii.b2a_hex(os.urandom(16)))
# passwd = input('password: ').encode()
# key = pbkdf2_hmac("sha256", passwd, salt, 50000, 32)
# print("Salt:", salt)
# print("Derived key:", binascii.hexlify(key))

# passwd = 'aaaa'.encode()
# key = pbkdf2_hmac("sha256", passwd, b'}JTQ90e\xa0\x8b*\xdd\xc0\x95\xea\xcb\x80', 50000, 32)
# print("Salt:", salt)
# print("Derived key:", binascii.hexlify(key))

# passwd = "b'}JTQ90e\xa0\x8b*\xdd\xc0\x95\xea\xcb\x80'".encode()
# print(passwd)
# passwd = passwd.decode()
# print(passwd)
# passwd = passwd.encode()
# print(passwd)

# salt = os.urandom(16)
# print(salt, type(salt))
# str_salt = str(salt)
# print(str_salt, type(str_salt))
# print(str_salt.encode(), str(salt).encode(), type(str(salt).encode()))
# print(str_salt.encode().decode(), type(str_salt.encode().decode()))
