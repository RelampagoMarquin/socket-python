import threading, time, random

mutex = threading.Lock()
Thread = threading.Thread
saldo = 0
fila = []
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

def executeFila():
    global fila
    while (len(fila) > 0):
        execute = fila[0]
        print(f'''
        ######################################
        INICIANDO PROCESSO de ID: {execute.id}
        ######################################
        ''')
        # Da maneira que a fila esta não vai funcionar o status, implementar fila na mão pode resolver
        """ while(execute.status == 'WAIT'):
            print('aguarde o outro processo encerrar')
            time.sleep(1) """
        
        execute.status = "EXECUTE"
        print('')
        execute.Thread.start()
        execute.status = 'DONE'
        print(f'''
        ######################################
        PROCESSO DE ID {execute.id} FINALIZADO
        ''' + execute.resultado)
        fila.pop(0)
        mutex.release()
    if(len(fila) == 0):
        return 'Aguardando Processo'

def addFila(processo):
    global fila
    fila.append(processo)
    return (f'Seu processo entrou na fila na posição: {len(fila)}')

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

print(f'Saldo atual: {saldo}')

p = Processo(custonThread(target=depositar, args=(10000,)))
fila.append(p)
for i in range(1, 10):
    action = random.randint(0, 1)
    valor = random.randint(10, 100)
    if(action == 1):
        p = Processo(custonThread(target=sacar, args=(valor,)))
        addFila(p)
    elif(action == 0):
        p = Processo(custonThread(target=depositar, args=(valor,)))
        addFila(p)
    
    executeFila()


