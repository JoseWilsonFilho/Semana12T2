#Calcular H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais.
# O número n é lido.

h = 0
numero = int(input())
for i in range(1,numero +1 ):
    h += (1 / i)
    i = numero - 1
print(f'{h:.4f}')
