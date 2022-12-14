import socket
import threading

lock = threading.Lock()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(1)

connection, address = server.accept()

def mult(arr):
    soma = int(arr[1])*int(arr[2])
    return soma

def div(arr):
    soma = int(arr[1])/int(arr[2])
    return soma

def soma(arr):
    soma = int(arr[1])+int(arr[2])
    return soma

def menos(arr):
    soma = int(arr[1])-int(arr[2])
    return soma

lock.acquire()
arr = connection.recv(1024).decode()
arr = arr.rsplit(',')
result = 0
if (arr[0] == "1" ):
    result = soma(arr)
elif(arr[0] == "2"):
    result = menos(arr)
elif(arr[0] == "3"):
    result = mult(arr)
elif(arr[0] == "4"):
    result = div(arr)
else:
    result = "opcao invalida"
lock.release()

connection.send(str(result).encode())
print('Fechando conexão.\n')
connection.close()
