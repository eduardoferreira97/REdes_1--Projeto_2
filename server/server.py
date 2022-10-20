import socket
import threading
import os

#49152-65535
class ThreadedServer():

    def __init__(self):
        
        self.host = socket.gethostname()
        self.port = 49159
        # Cria o socket
        # F_INET (família de endereço IPV4) e SOCK_STREAM (TCP)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))                          
                                                                     

    def listen(self):
        # Habilita que o servidor aceite conexões
        self.s.listen(5)
        while True:
            # Aceit a conexão do cliente no servidor
            c, addr = self.s.accept()
            # Permite que mais de um cliente utilizem o servidor
            threading.Thread(target = self.listenToClient,args = (c,addr)).start()

    def listenToClient(self, c, addr):

        print('Conexão estabelecida', addr)

        
        # Recebe a ação do cliente
        data = c.recv(1024)


        if (data.decode() == "download"):
            # Recebe o nome do arquivo
            FileName = c.recv(1024)

            # Percorrer o diretório
            for file in os.listdir("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server"):

                if file == FileName.decode():
                    FileFound = 1
                    break

            if FileFound == 0:
                # Caso o arquivo não exista, ele printaque o arquivo não existe.
                c.send()
                print("Não encontrado no servidor")

            else:
                # Caso o arquivo exista, ele vai decodificar as suas informações
                
                upfile = FileName.decode()
                # Abri o arquivo em binário para ser lido
                UploadFile = open("/home/eduardo/Documentos/Projetos/Redes 1/Projeto 2/server//"+upfile,"rb")
                Read = UploadFile.read(1024)

                # Envia o arquivo lido 
                while Read:
                    c.send(Read) #Envia 1KB 
                    Read = UploadFile.read(1024)

                print("Arquivo baixado")
                # Fecha as conexões
                UploadFile.close()
                c.close()

        elif (data.decode() == "upload"):
            # Recebe o nome do arquivo
            FileName = c.recv(1024)
            downfile = FileName.decode()

            Data = c.recv(1024)
            # Abrindo o arquivo que vai ser baixado
            DownloadFile = open(downfile,"wb")
            # Loop para "escrever" o arquivo selecionado
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
