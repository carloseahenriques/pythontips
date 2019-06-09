

import hashlib

print (hashlib.md5((open("/path/para/o/arquivo.foo").read)().encode('utf-8')).hexdigest())
