import socket               
import os

#49152-65535
class Cliente:

    def __init__(self):
        self.s = socket.socket()         
        self.host = socket.gethostname() 
        self.port = 49157                
        self.s.bind((self.host, self.port))   

        try:
            
            self.s.connect((self.host, 49159))
            print("Conecatado com sucesso!")
        except Exception as e: 
            print("Tem alguma coisa errada com %s:%d. O erro é %s" % (self.host, 49159, e))
            
    def rodando(self):
# while True:
        Answer = input("download/ upload/ exit: ")

        if(Answer == "download"):

            mssg = "download"
            self.s.send(mssg.encode())
            print("Arquivos:")
            for arq in os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server"):
                print(arq)
            print("\n")
            FileName = input("Digite o nome do arquivo que vai ser baixado: ")
            Data = "Temp"

            while True:

                self.s.send(FileName.encode())
                Data = self.s.recv(1024)
                DownloadFile = open(FileName,"wb")

                while Data:

                    DownloadFile.write(Data)
                    Data = self.s.recv(1024)
                
                print("Arquivo baixado")
                DownloadFile.close()
                break
                
        elif(Answer == "upload"):

            mssg = "upload"
            self.s.send(mssg.encode())

            print("Arquivos:")
            for arqs in os.listdir(os.getcwd()+"/files"):
                print(arqs)
            print("\n")
            
            FileName = input("Coloque o nome o arquivo que vai ser eniado: ")
            self.s.send(FileName.encode())

            UploadFile = open("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/client/files//"+FileName,"rb")
            Read = UploadFile.read(1024)
                
            while Read:
                self.s.send(Read) #Envia 1KB 
                Read = UploadFile.read(1024)
            print("Arquivo enviado")
            UploadFile.close()

        elif(Answer == "exit"):
            mssg = "exit"
            print("Saindo do servidor")
            self.s.send(mssg.encode())
            
            self.s.close()

if __name__ == "__main__":
    c1 = Cliente()
    c1.rodando()


