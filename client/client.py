import socket               
import os

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

while True:
    Answer = input("download/ upload/ exit: ")

    if(Answer == "download"):

        mssg = "download"
        s.send(mssg.encode())
        print("Arquivos:")
        for arq in os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server"):
            print(arq)
        print("\n")
        FileName = input("Digite o nome do arquivo que vai ser baixado: ")
        Data = "Temp"

        while True:

            s.send(FileName.encode())
            Data = s.recv(1024)
            DownloadFile = open(FileName,"wb")

            while Data:

                DownloadFile.write(Data)
                Data = s.recv(1024)
            
            print("Arquivo baixado")
            DownloadFile.close()
            break
            
    elif(Answer == "upload"):

        mssg = "upload"
        s.send(mssg.encode())

        print("Arquivos:")
        for arqs in os.listdir(os.getcwd()+"/files"):
            print(arqs)
        print("\n")

        FileName = input("Coloque o nome o arquivo que vai ser eniado: ")
        s.send(FileName.encode())

        UploadFile = open("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/client/files//"+FileName,"rb")
        Read = UploadFile.read(1024)
            
        while Read:
            s.send(Read) #Envia 1KB 
            Read = UploadFile.read(1024)
        print("Arquivo enviado")
        UploadFile.close()

    elif(Answer == "exit"):
        mssg = "exit"
        print("Saindo do servidor")
        s.send(mssg.encode())
        break
s.close()




