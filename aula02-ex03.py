import os
os.system('cls')
"""
Exercicio 3
– Faça uma aplicação que apresente em tela a tabuada de qualquer número.
 – O usuário fornece o número desejado e a aplicação apresenta a relação de todos os cálculos de 1 a 10
"""

def tabuada(valor):
    for i in range(10):
        print("{0} x {1} = {2}".format(valor, i+1, valor*(i+1)))

def input_inicial():
    valor = int(input("Vamos lá, digite o número da tabuada que vc quer ;)\n"))
    os.system('cls')
    tabuada(valor)

jogar = ""
while (jogar == ""):
    os.system('cls')
    input_inicial()
    jogar = input("Pressione enter pra jogar de novo")