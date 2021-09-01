import os
os.system('cls')

"""
Ex.1
Elabore uma aplicação que receba o nome de um produto e o seu valor. 
O desconto deve ser calculado de acordo com o valor fornecido conforme a Tabela. 
Apresente em tela o nome do produto, valor original do produto e o novo valor depois de ser realizado o desconto. 
Caso o valor digitado seja menor que zero, deve ser emitida uma mensagem de aviso. 
"""
def descontos(valor):
    desconto = 0
    if(valor < 50):
        desconto = 0;
    elif valor < 200:
        desconto = 5;
    elif valor < 500:
        desconto = 6;
    elif valor < 1000:
        desconto = 7;
    else:
        desconto = 8;
    return desconto


def input_inicial():
    nome = input("Insira o nome do produto: ")
    valor = float(input("\nInsira o valor do produto: "))
    
    while(valor < 0):
        print("Valor inválido, tente novamente\n")
        valor = float(input("\nInsira o valor do produto: "))

    os.system('cls')
    print("Nome do produto: {0}\nValor original: {1}\nDesconto: {2}%\nValor com desconto: {3}".format(nome, valor, descontos(valor), float(valor-(valor*(descontos(valor)/100)))))

input_inicial()