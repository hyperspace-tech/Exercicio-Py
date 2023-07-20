numero = int(input("Informe um numero: "))

if numero % 2 == 0:
    if numero > 0:
        print("O numero {0} e par e positivo".format(numero))
    else:
        print("O numero {0} e par e negativo".format(numero))
else:
    if numero > 0:
        print("O numero {0} e impar e positivo".format(numero))
    else:
        print("O numero {0} e impar e negativo".format(numero))