import sys
import os
import collections
import json 

Produto = collections.namedtuple("Produto","codProduto produto valorCompra valorVenda qtdEstoque")
produtos=[]
codProduto = 1

def Inicio():
    os.system('cls')
    print("[1] Cadastrar de produto\n[2] Relatório de produtos\n[3] Relatório de Estoque Baixo\n[4] Exportar dados\n[5] Sair")
    ans = 0
    while not ans:
            try:
                ans = int(input())
                if ans not in (1, 2, 3, 4, 5):
                    raise ValueError
            except ValueError:
                ans = 0
                print("Opção inválida!")
                return Inicio()

    if ans == 1:
        cadastra_produto()
        return Inicio()
    if ans == 2:
        lista_produto(produtos)
        return Inicio()
    if ans == 3:
        lista_produto(produtos, True)
        return Inicio()
    if ans == 4:
        exportar()
        return Inicio()
    elif ans == 5:
        print('Saindo!')
        sys.exit
    else:
        print('Opção inválida!')
    return None  
 
def cadastra_produto():
    global codProduto
    produto = input("Descricao Produto\n")
    valorCompra = input("Valor do Produto\n")
    qtdEstoque = input("Estoque Produto\n")
    valorCompra=float(valorCompra)
    valorVenda=float(1.25*valorCompra)
    qtdEstoque=int(qtdEstoque)
    produtos.append(Produto(codProduto,produto,valorCompra,valorVenda,qtdEstoque))
    codProduto = codProduto+1
    
 
def ordenar_lista(produtos):
    n = len(produtos)
      
    for i in range(n):
        for j in range(n-i-1):
              
            if produtos[j][1] > produtos[j + 1][1]:
                produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]
                  
    return produtos
 
    
def lista_produto(produtos, estoque_baixo = False):
    produtos_ordenados=ordenar_lista(produtos)
    if(estoque_baixo == True):
            print("Produtos com estoque em baixa")
    for i in produtos_ordenados:
        if(estoque_baixo == True):
            if(i.qtdEstoque < 5):
                print("-------------------------------------------------------------")
                print("Codigo do produto: %d" %i.codProduto)
                print("Nome do produto  : %s" %i.produto)
                print("Valor de compra  : %.2f" %i.valorCompra)
                print("Valor de venda   : %.2f" %i.valorVenda)
                print("Qtd em estoque   : %d" %i.qtdEstoque)
                print("-------------------------------------------------------------")
        if(estoque_baixo == False):
            print("-------------------------------------------------------------")
            print("Codigo do produto: %d" %i.codProduto)
            print("Nome do produto  : %s" %i.produto)
            print("Valor de compra  : %.2f" %i.valorCompra)
            print("Valor de venda   : %.2f" %i.valorVenda)
            print("Qtd em estoque   : %d" %i.qtdEstoque)
            print("-------------------------------------------------------------")
    espera = input("aperta qualquer tecla pra continuar")

def exportar():
    g = open("produtos.json","w")
    json.dump(produtos,g,indent=5)
    g.close()
    print("Exportado com sucesso!")
    input('...')

Inicio()