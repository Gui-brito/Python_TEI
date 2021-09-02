f = open("countries.txt","r")
lista = []
with open("teste.txt","w") as x:
    for i in f:
        x.write(i);
        x.write('\n')


f.close()

