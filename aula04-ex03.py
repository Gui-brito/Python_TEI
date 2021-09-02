i = input("Qual palavra quer achar?")
f = open("countries.txt","r")
lista = []
for j in f:
    lista.append(j.strip())

print(lista.count(i))

