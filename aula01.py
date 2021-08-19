import os
os.system('cls')
"""
Exercicio 1 - Crie uma aplicação que receba o valor da base e da altura 
de um triângulo retângulo e apresente na tela sua área

"""
altura = float(input("Qual é a altura do triangulo, em centimetros? "))
base = float(input("E qual é a base, também em centimetros? "))

area = (altura*base)/2

print("Fiz as contas aqui e a area do seu triangulo é %.2f\n\n" %area)
input("Pressione qualquer tecla para o próximo exercicio...")

os.system('cls')
"""
Exercicio 2 - Crie um programa para calcular e exibir na tela o peso ideal. IMC = (peso / (altura^2)

"""
altura_imc = float(input("Qual é a sua altura? em metros"))
peso_imc = float(input("Qual é o seu peso? Em kg "))

aux = altura_imc*altura_imc

imc = (peso_imc/aux)
print(imc)

print("Fiz as contas aqui e o seu IMC é %.2f\n\n" %imc)
if(imc < 18.5):
    print("Você está abaixo do peso")
elif(imc < 25):
    print("Você está no peso ideal")
elif(imc < 30):
    print("Você está levemente acima do peso")
elif(imc < 35):
    print("Obesidade I")
elif(imc < 40):
    print("Obesidade II (Severa)")
else:
    print("Obesidade III (Mórbida)")


input("Pressione qualquer tecla para o próximo exercicio...")

os.system('cls')