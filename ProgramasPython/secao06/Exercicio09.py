indice = float(input("Informe o indice de poluicao: "))
if indice >= 0.3 and indice < 0.4:
    print("ATENCAO: industrias do primeiro gupo devem suspender as atividades")
elif indice >= 0.4 and indice <0.5:
    print("ATENCAO: industrias do segundo grupo devem suspender as atividades")
elif indice > 0.5:
    print("ATENCAO TODOS GRUPOS DEVEM SUSPENDER OS SERVICOS! ")