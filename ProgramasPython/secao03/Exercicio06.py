valor_por_hora = float(input("Quanto voce quanha por hora? "))
horas_trabalhadas = float(input("quantas horas voce trabalhou esse mes? "))

salario = horas_trabalhadas * valor_por_hora

print("nesse mes voce ira receber R${0:.2f}".format(salario))
