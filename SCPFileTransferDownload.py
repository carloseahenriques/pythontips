

import subprocess
import os

FileTransferDownload = subprocess.Popen(["scp", "usuario@192.168.10.1:/home/usuario/Arquivo.txt", "/home/usuario/Arquivo_com_Novo_Nome.txt"])
sts = os.waitpid(FileTransferDownload.pid, 0)
