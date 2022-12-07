import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(1)

connection, address = server.accept()

soma=0
def mult(arr):
    soma = float(arr[1])*float(arr[2])
    return soma

def div(arr):
    soma = float(arr[1])/float(arr[2])
    return soma

def soma(arr):
    soma = float(arr[1])+float(arr[2])
    return soma

def menos(arr):
    soma = float(arr[1])-float(arr[2])
    return soma

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

connection.send(str(result).encode())
print('Fechando conexão.\n')
connection.close()
