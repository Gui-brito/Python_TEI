import json

f = open("arquivo.csv","r")
lista = []
for i in f:
    lista.append(i.strip().replace(',',", "))
g = open("output.json","w")

#escrever formato JSON
json.dump(lista,g,sort_keys=True)
f.close()
g.close()

print(lista)