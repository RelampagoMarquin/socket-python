import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print ('Cliente conectado.\n')
arr = '1'

def menu():
    selecao = 'n' 
    num1 ='n'
    num2 ='n'
    text = 'você digitou um caractere que não é um número inteiro'
    while not (selecao.isnumeric()):
        print('DIGITE APENAS O NUMERO: \n 1 - SOMA \n 2 - SUBTRACAO \n 3 - MULTIPLICACAO \n 4 - DIVISAO')
        selecao = str(input('DIGITE O NUMERO DA OPERACAO QUE DESEJA FAZER: '))
        if (selecao == '5'):
            return 'Finalizando'
        if not (selecao.isnumeric()):
            print (text)
    while not(num1.isnumeric()):
        num1 = str(input('DIGITE O NUMERO(dividendo em caso de divisao): '))
        if not (num1.isnumeric()):
            print (text)
    while not(num2.isnumeric()):
        num2 = str(input('DIGITE O NUMERO(divisor em caso de divisao): '))
        if not (num2.isnumeric()):
            print (text)

    arr = selecao+','+num1+','+num2
    return arr
    

try:
    lista = menu()
    client.send(lista.encode())
    data = client.recv(1024).decode()
    print(f"Resultado: " + data)
except socket.error as e: 
    print ("Socket error: %s" %str(e)) 
except Exception as e: 
    print ("Other exception: %s" %str(e)) 
finally: 
    print ("Closing connection to the server") 
    client.close() 
