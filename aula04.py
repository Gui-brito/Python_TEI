import os
os.system('cls')

# lista1 = [1,2,3,'vish',['nome','Guilherme']]

# for item in lista1:
#     print(item)

# lista1.insert(1,'teste')


# for item in lista1:
#     print(item)

# lista1 = [1,9,2,3]
# lista2 = [4,5,6]
# lista3 = []

# lista3.extend(lista1+lista2)
# lista3.sort()
# for item in lista3:
#     print(item)

def exibir (lista):
    for item in lista:
        print(item)

    print("tamanho = %d \n" %len(lista))

# lista = [5,2,3,4]
# lista.sort()
# lista.insert(0,1)
# lista.reverse()
# lista.remove(2)
# del lista[1]
# exibir(lista)

letras = ["A","B","C"]
numeros = [1,2,3]

prod_cart = [(let,num) for let in letras for num in numeros]
exibir(prod_cart)
