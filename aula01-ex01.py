import os
os.system('cls')
"""
Exercicio 1 - Crie uma aplicação que receba o valor da base e da altura 
de um triângulo retângulo e apresente na tela sua área

"""
def imc():
    altura = float(input("Qual é a altura do triangulo, em centimetros? "))    
    base = float(input("E qual é a base, também em centimetros? "))
    return (altura*base)/2


print("Fiz as contas aqui e a area do seu triangulo é %.2f cm²\n\n" %imc())


