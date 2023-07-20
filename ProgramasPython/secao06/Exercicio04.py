altura = float(input("informe sua altura: "))
sexo = input("informe seu sexo m/f: ")

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) -58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) -44.7
else:
    peso_ideal = 0
    print("sexo nao indentificado")
print("Seu peso_ideal e {0:.2f}".format(peso_ideal))