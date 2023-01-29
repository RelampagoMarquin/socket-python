import threading, time

mutex = threading.Lock()
Thread = threading.Thread
valor = 1000

def depositar (deposito):
    global valor, mutex
    mutex.acquire()
    oldValor = valor
    valor += deposito
    print(f'''
    ############ EXTRATO ############
    # Valor Anterior: {oldValor} R$
    # Valor Depositado: {deposito} R$
    # Saldo Atual: {valor} R$
    #################################
    ''')
    mutex.release()
    print('''
    #################################
    ## THREAD FINALIZADA ############
    #################################
    ''')

def sacar (sacado):
    global valor, mutex
    mutex.acquire()
    oldValor = valor
    valor -= sacado
    print(f'''
    ############ EXTRATO ############
    # Valor Anterior: {oldValor} R$
    # Valor Sacado: {sacado} R$
    # Saldo Atual: {valor} R$
    #################################
    ''')
    mutex.release()
    print('''
    #################################
    ## THREAD FINALIZADA ############
    #################################
    ''')

print(f'Saldo atual: {valor}')
Thread(target=sacar, args=(300,)).start()
Thread(target=depositar, args=(100,)).start()


