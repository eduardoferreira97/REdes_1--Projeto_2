import socket
import threading
import os

#49152-65535
class ThreadedServer():
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 49159
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))                          
                                                                     
        

    def listen(self):
        self.s.listen(5)
        while True:
            c, addr = self.s.accept()
            # c.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (c,addr)).start()

    def listenToClient(self, c, addr):
        # block_size = 1024
        print('Conexão estabelecida', addr)

        data = c.recv(1024)
    
        if (data.decode() == "download"):
            FileName = c.recv(1024)
            for file in os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server"):
                if file == FileName.decode():
                    FileFound = 1
                    break

            if FileFound == 0:
                print("Não encontrado no servidor")

            else:
                print("Arquivo baixado")
                upfile = FileName.decode()
                UploadFile = open("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server//"+upfile,"rb")
                Read = UploadFile.read(1024)

                while Read:
                    c.send(Read) #Envia 1KB 
                    Read = UploadFile.read(1024)
                UploadFile.close()
                c.close()

        elif (data.decode() == "upload"):
            FileName = c.recv(1024)
            downfile = FileName.decode()
            Data = c.recv(1024)
            DownloadFile = open(downfile,"wb")
            
            while Data:
                DownloadFile.write(Data)
                Data = c.recv(1024)
               
            print("Arquivo enviado")
            DownloadFile.close()
            c.close()
        
        elif data.decode() == "exit":
            print("Saindo do servidor")
            c.close()
        
                 
if __name__ == "__main__":
    ThreadedServer().listen()
