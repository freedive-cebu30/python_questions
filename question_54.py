# coding: utf-8


import hashlib

dat = 'a' 

hs_md5 = hashlib.md5(dat.encode()).hexdigest()
hs_sha256 = hashlib.sha256(dat.encode()).hexdigest()
hs_sha512 = hashlib.sha512(dat.encode()).hexdigest()
print(hs_md5)
print(hs_sha256)
print(hs_sha512)
