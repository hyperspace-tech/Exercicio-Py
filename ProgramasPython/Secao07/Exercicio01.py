maior = 0
n = int(input("Informe um numero: "))
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Informe um numero: "))
print(" o maior numero e {0}".format(maior))