

import subprocess
import os

FileTransferUpload = subprocess.Popen(["scp", "/root/MeuArquivo.txt", "usuario@nv192.168.10.1:/home/usuario/"])
sts = os.waitpid(FileTransferUpload.pid, 0)
