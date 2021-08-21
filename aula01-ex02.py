import os
os.system('cls')
"""
Exercicio 2 - Crie um programa para calcular e exibir na tela o peso ideal. IMC = (peso / (altura^2)

"""
def imc():
    altura_imc = float(input("Qual é a sua altura? em metros\n"))
    menor_peso = 18.5*(altura_imc*altura_imc)
    maior_peso =  24.9*(altura_imc*altura_imc)
    return print("O peso ideal fica entre ", round(menor_peso,2), " e ", round(maior_peso,2)," Kg")

imc();