

import hashlib

inputfile=(open("/path/para/o/arquivo.foo").read)
print (hashlib.md5(inputfile().encode('utf-8')).hexdigest())
