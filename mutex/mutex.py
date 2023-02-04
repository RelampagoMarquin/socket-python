import threading, time, random

mutex = threading.Lock()
Thread = threading.Thread
saldo = 1000

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

class Processo():
    def __init__(self, custonThread):
        self._id = random.randint(1, 100)
        self._status = 'WAIT'
        self._Thread = custonThread
        self._resultado = ''

    @property
    def status(self):
        return self._status

    @property
    def resultado(self):
        self._resultado = self.Thread.join()
        return self._resultado

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def Thread(self):
        return self._Thread

    @property
    def id(self):
        return self._id

class Node:
    # Cria o node
    def __init__(self, data):
        self.data = data  # salva o dado
        self.anterior = None
        self.proximo = None  # inicializa o proximo como null
  
# Linked List class
class LinkedList:
    
    # Cria a Linked List
    def __init__(self): 
        self.head = None
        self.end = None
        self.length = 0

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def enQueue(self, new_data):
  
        new_node = Node(new_data)
  
        if self.head is None:
            self.head = new_node
            self.head = new_node
            return new_node.data

        else:
            current = self.head
            while (current.proximo):
                current = current.proximo
  
            current.proximo =  new_node
            new_node = current
            self.end = new_node

        self.length += 1
        return new_node.data
    
    def deQueue(self):
        start = self.head
        if(start):
            if(start.anterior):
                start.anterior = None
            else:
                self.end = None
            self.head = self.head.proximo
        else:
           raise Exception('Fila vazia')
        self.length -= 1
        return start.data


    # Enquanto houver elementos ele faz o print
    def printList(self):
        temp = self.head
        print('A lista criada é: ')
        while (temp):
            print (temp.data)
            temp = temp.proximo

def executeFila(fila):
    while (fila.size() > 0):
        execute = fila.head.data
        print(f'''
        ######################################
        INICIANDO PROCESSO de ID: {execute.id}
        ######################################
        ''')
        execute.status = "EXECUTE"
        print('')
        execute.Thread.start()
        print(f'''
        ######################################
        PROCESSO DE ID {execute.id} FINALIZADO
        ''' + execute.resultado)
        execute.status = 'DONE'
        fila.deQueue()
        mutex.release()
    if(fila.isEmpty):
        print('Aguardando Processo')

def addFila(fila, processo):
    fila.enQueue(processo)
    return (f'Seu processo entrou na fila na posição: {fila.size()+1}')

def depositar (deposito):
    global saldo, mutex
    mutex.acquire()
    oldValor = saldo
    saldo += deposito
    return(f'''
        ############ EXTRATO ############
        # Valor Anterior: {oldValor} R$
        # Valor Depositado: {deposito} R$
        # Saldo Atual: {saldo} R$
        #################################
    ''')
    
def sacar (sacado):
    global saldo, mutex
    mutex.acquire()
    oldValor = saldo
    saldo -= sacado
    return(f'''
        ############ EXTRATO ############
        # Valor Anterior: {oldValor} R$
        # Valor Sacado: {sacado} R$
        # Saldo Atual: {saldo} R$
        s#################################
    ''')


#Teste

print(f'Saldo atual: {saldo}')

fila = LinkedList()

for i in range(0, 10):
    executeFila(fila)
    action = random.randint(0, 1)
    valor = random.randint(10, 100)
    if(action == 1):
        p = Processo(custonThread(target=sacar, args=(valor,)))
        print(addFila(fila, p))
    elif(action == 0):
        p = Processo(custonThread(target=depositar, args=(valor,)))
        print(addFila(fila, p))
    
    


