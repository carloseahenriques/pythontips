

import requests

# Primeiramente instale o módulo "requests" [ pip install requests ]
# Documentação detalhada do módulo no site do projeto:
# https://realpython.com/python-requests/

RequisicaoHttp = (requests.get("http://ifconfig.me"))
RequisicaoHttp.content
print (RequisicaoHttp.content.decode('utf-8'))
