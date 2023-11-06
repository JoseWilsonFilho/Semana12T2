

a, b = 0 ,1
numero = int(input())
sequencia= ''

for i in range(numero):
    sequencia += str(a)+',' + ' '
    a, b = b , a + b

valor = sequencia[:-2]
print(f'{valor}')

