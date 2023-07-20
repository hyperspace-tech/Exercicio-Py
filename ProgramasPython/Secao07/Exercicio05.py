nome = input("Informe o usuario: ")
senha = input("Informe sua senha: ")

while nome == senha:
    print(" Erro: o nome e senha devem ser diferentes !")
    nome = input("Informe o usuario: ")
    senha = input("Informe a senha: ")