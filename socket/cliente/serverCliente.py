import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print ('Cliente conectado.\n')

namefile = str(input('Digite o arquivo a ser baixado: '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(10000000)# O numero no recv representa o tamanho do arquivo
        print(data)
        if data == b'':
            break
        else: 
            file.write(data)
    print(f'{namefile} RECEBIDO.\n')
    
    