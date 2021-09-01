import os
"""
Exercicio 5 
– Elabore uma aplicação que receba o peso e altura de um número indeterminado de pessoas.
 – Utilize tratamento de exceção para garantir que os valores informados são válidos. 
 – Após a entrada correta dos dados apresente o IMC.
  – Para cada entrada de dados pergunte ao usuário “Deseja continuar?

"""
while True:
    os.system('cls')
    try:
        altura = float(input("Qual é a altura do triangulo, em centimetros? "))    
        base = float(input("E qual é a base, também em centimetros? "))
    except ValueError:
        print("Valor Incorreto")
    finally:
        print((altura*base)/2)
        if input("Deseja jogar de novo? Tecle N para encerrar ") == "N":
            break