
"""
Atividade prática final
Exercicio 1 
"""
import os
os.system('cls')

import string
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.


def nome_plausivel(nome):
    if " "  not in nome:
        return False
    else:
        return True

def trata_username(nome):
    nomes_exclude = ['Junior','Filho','Neto', 'Jr']

    if nome.split()[-1] not in nomes_exclude:
        sobrenome = nome.split()[-1]
    else:
        sobrenome = nome.split()[-2]
    username = nome[0]+sobrenome
    return username

def senha_aleatoria():
    


nome = input("Digite o nome completo do aluno\n")

while(nome_plausivel(nome) == False):
    os.system('cls')
    print("Digite um nome plausivel")
    nome = input("Digite o nome completo do aluno\n")
    
username = trata_username(nome)



# os.system('cls')


# dic = dict({"Nome":nome, "Username":nome.split()[0][0]+sobrenome})

# for chave,valor in dic.items():
#     print("%s = %s" %(chave,valor))