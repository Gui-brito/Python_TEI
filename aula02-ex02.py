import os
os.system('cls')
"""
Exercicio 2
– Na área da eletrônica, em um circuito em série temos que a resistência equivalente (total)
 desse circuito é obtida mediante a soma de todas as resistências existentes (RE = r1 + r2 + ... + rn). 
 – Faça uma aplicação que receba o valor de quatro resistências ligadas em série.
 Calcule e mostre a resistência equivalente, a maior e a menor resistência.
"""

def maior(valores):
    valores.sort()
    return valores[-1]

def menor(valores):
    valores.sort()
    return valores[0]

def resistencia_total(valores):
    total = 0
    for i in valores:
        total += i
    return total


def input_inicial():
    valores = []
    for i in range(4):
        ele = float(input("Insira o valor da resistencia {0}: ".format(i+1)))
        valores.append(ele)
        os.system('cls')    

    print("O maior valor das resistencias é {0}\nO menor é {1}\nE a resistencia equivalente desse circuito é {2}".format(float(maior(valores)), float(menor(valores)), float(resistencia_total(valores))))
    
input_inicial()