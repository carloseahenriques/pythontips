

import subprocess

from subprocess import PIPE, Popen

ComandoARodarNaMaquinaRemota = 'uname -a'
stream = Popen(['ssh', 'root@192.168.10.1', ComandoARodarNaMaquinaRemota],stdin=PIPE, stdout=PIPE)
rsp = stream.stdout.read().decode('utf-8')
print(rsp)
