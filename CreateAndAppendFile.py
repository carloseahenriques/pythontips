

def CreateAndAppendFile(filename, content):
	with open(filename, "a") as myfile:
	    myfile.write(content)
CreateAndAppendFile("MeuArquivo.txt","Minha Mensagem com quebra de linha \n")
