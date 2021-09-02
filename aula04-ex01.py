import os
os.system("cls")

n = int(input("Quantas linhas deseja ler? "))

f = open("countries.txt", "r", encoding="utf8")

for i in range(n):
    linha = f.readline()
    print(linha)

f.close()
