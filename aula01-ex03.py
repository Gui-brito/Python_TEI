"""
Exercício 3 
Uma farmácia precisa ajustar os preços de seus produtos em 12%.
Elabore uma aplicação que receba o valor do produto e aplique o percentual de acréscimo.
O novo valor a ser calculado deve ser arredondado e apresentado com duas casas decimais.
"""

def ajuste():
    preco = float(input("Insira o valor do produto\n"))
    return print("O valor ajustado é R$ ", round(preco+(preco*0.12),2))
    
ajuste();