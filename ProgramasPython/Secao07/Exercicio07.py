contador_total = 0
contador_sit1 = 0
contador_sit2 = 0
contador_sit3 = 0
contador_sit4 = 0

identificador = int(input("informe a identificacao: "))

while identificador != 0:
    print("1- Necessidade de esfera.")
    print("2- Necessidade de limpeza.")
    print("3- troca do cabo ou conector.")
    print("4- quebrado ou inutilizado.")
    
    defeito = int(input("Informe o defeito: "))
    
    if defeito == 1:
        contador_sit1 = contador_sit1 + 1
    elif defeito == 2:
        contador_sit2 = contador_sit2 + 1
    elif defeito == 3:
        contador_sit3 = contador_sit3+ 1
    elif defeito == 4:
        contador_sit4 = contador_sit4 + 1
    contador_total = contador_total + 1
    
    identificador = int(input("informe a identificacao: "))
    
p1 = contador_sit1 / contador_total * 100.0
p2 = contador_sit2 / contador_total * 100.0
p3 = contador_sit3 / contador_total * 100.0
p4 = contador_sit4 / contador_total * 100.0
print("Situacao                    quantidade       percentual")
print("1 - nescessidade de esfera        {0}           {1:.2f}%".format(contador_sit1, p1))
print("2 - nescessidade de limpeza       {0}           {1:.2f}%".format(contador_sit2, p2))
print("3 - troca do cabo ou conector     {0}           {1:.2f}%".format(contador_sit3, p3))
print("4 - nescessidade de esfera        {0}           {1:.2f}%".format(contador_sit4, p4))