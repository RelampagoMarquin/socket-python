import socket
from threading import Thread, Lock

#this is thread?
# YES!!, basicamente é uma herança que adiciona o retorno 
class custonThread(Thread):
    #inicia a thread adicionando a variavel de retorno
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    
    #sobescreve o da threah run(), como dito na dumentação, isso pode acontecer
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    
    # sobreescreve o metodo de join() e retorna o valor do metodo
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind (('localhost', 7777))
print('Aguardando conexões.\n')
server.listen(1)

connection, address = server.accept()

def mult(arr):
    result = int(arr[1])*int(arr[2])
    return result

def div(arr):
    result = int(arr[1])/int(arr[2])
    return result

def soma(arr):
    result = int(arr[1])+int(arr[2])
    return result

def menos(arr):
    result = int(arr[1])-int(arr[2])
    return result

Lock().acquire
arr = connection.recv(1024).decode()
arr = arr.rsplit(',')
result = 0
if (arr[0] == "1" ):
    ct = custonThread(target=soma, args=(arr,))
    ct.start() #para confirma que é uma thread ele start com metodo padrão
    result = ct.join()
elif(arr[0] == "2"):
    ct = custonThread(target=menos, args=(arr,))
    ct.start()
    result = ct.join()
elif(arr[0] == "3"):
    ct = custonThread(target=mult, args=(arr,))
    ct.start() #para confirma que é uma thread ele start com metodo padrão
    result = ct.join()
elif(arr[0] == "4"):
    ct = custonThread(target=div, args=(arr,))
    ct.start() #para confirma que é uma thread ele start com metodo padrão
    result = ct.join()
Lock().release

try:
    connection.send(str(result).encode())
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Other exception: %s" %str(e)) 
finally: 
    print ("Closing connection to the client") 
    connection.close() 