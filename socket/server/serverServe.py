import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(1)

connection, address = server.accept()
namefile = connection.recv(1024).decode()

try:
    os.path.isfile(f"./{namefile}")
    with open (namefile, 'rb') as file:
        for data in file.readlines():
            connection.send(data)
        
    print('Arquivo enviado com sucesso')

except:
    print('Arquivo não encontrado.')

