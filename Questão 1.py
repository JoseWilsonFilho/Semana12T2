#Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que: N ! = 1 x 2 x 3 x ... x N-1 x N 0 ! = 1

numeros = int(input())
fatorial = 1
contador = 1
while contador <= numeros:
    fatorial *= contador
    contador += 1
print(fatorial)




a, b = 0 ,1
numero = int(input())
sequencia= ''

for i in range(numero):
    sequencia += str(a)+ ',' + ' '
    a, b = b , a + b
    sequencia = sequencia.strip()
    sequencia = sequencia[:-1]
print(f'{sequencia}')

