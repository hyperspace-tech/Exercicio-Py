valor_hora = 10.00
valor_horas_excedente = 20.00
e = 0

c = int(input("Informe o codigo: "))
n = float(input("Informe a quantidade de horas trabalhadas: "))

if n > 50:
    e = (n -50) * valor_horas_excedente
    salario = (50 * valor_hora) + e
    print("salario Total R$ {0:.2f}".format(salario))
    print("salario excedente R$ {0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("salario Total R$ {0:.2f}".format(salario))
    print("salario excedente R$ {0:.2f}".format(e))