import re

def valida(usuario, senha):
    if re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$",senha):
        print(f"Senha dentro do padrão {senha}")
    else:
        print(f"Senha fora do padrão {senha}")

usuario = input("Entre com o usuário: ")
senha = input("Entre com a senha: ")
valida(usuario, senha)