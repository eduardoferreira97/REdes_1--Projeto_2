import socket               
import os
import time
from tqdm import tqdm

#49152-65535
s = socket.socket()         
host = socket.gethostname() 
port = 49157                

s.bind((host, port))   

try:
    s.connect((host, 49159))
    print("Conecatado com sucesso!")
except Exception as e: 
    print("Tem alguma coisa errada com %s:%d. O erro é %s" % (host, 49159, e))

Answer = input("download/ upload/ exit: ")
if(Answer == "download"):
    mssg = "download"
    s.send(mssg.encode())
    print("Arquivos:\n")

    for arq in os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/client/files"):
        print(arq)
    FileName = input("Digite o nome do arquivo que vai ser baixado: ")
    Data = "Temp"

    while True:
        s.send(FileName.encode())
        Data = s.recv(1024)
        DownloadFile = open(FileName,"wb")
        i = 1
        while Data:
            # print('Baixando...%d' %(i))
            # for i in tqdm(range(1)):
            #     time.sleep(1)
            DownloadFile.write(Data)
            Data = s.recv(1024)
            i = i + 1
        print("Arquivo baixado")
        DownloadFile.close()
        break
    
elif(Answer == "upload"):
    mssg = "upload"
    s.send(mssg.encode())
    print(os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/client/files"))
    FileName = input("Coloque o nome o arquivo que vai ser eniado: ")
    s.send(FileName.encode())

    UploadFile = open("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/client/files//"+FileName,"rb")
    Read = UploadFile.read(1024)
    i = 1
    while Read:
        # Problema no range do arquivo, não consigo pegar o tamanho exato
        # for i in tqdm(range(len(Read))):
        #     time.sleep(1)

        s.send(Read) #Envia 1KB 
        Read = UploadFile.read(1024)
    print("Arquivo enviado")
    UploadFile.close()

elif(Answer == "exit"):
    mssg = "exit"
    print("Saindo do servidor")
    s.send(mssg.encode())
s.close()




