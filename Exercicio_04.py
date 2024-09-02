print("Descobrindo as lógicas:")

print("A)", end=' ')  #contando de dois em dois
for i in range(1, 10, 2):
    print(i, end=', ')


print("\nB)", end=' ') #somando os números
numero = 2
while numero <= 128:
    print(numero, end=', ')
    numero *= 2


print("\nC)", end=' ') #quadrado do numero
for i in range(8): 
    quadrado = i * i
    print(quadrado, end=', ')


print("\nD)", end=' ') #quadrado de cada valor, o prox valor ao quadrado é 10 sendo 100 a resposta
for i in range(2, 12, 2):  
    quadrado = i * i
    print(quadrado, end=', ')


print("\nE)", end=' ') #sequência de Fibonacci
a, b = 1, 1
print(a, end=', ')
print(b, end=', ')
for v in range(5):  
    a, b = b, a + b
    print(b, end=', ')


print("\nF)", end=' ') #sequencia 
sequencia = [2, 10, 12, 16, 17, 18, 19]

proximo_numero = sequencia[-1] + 1
sequencia.append(proximo_numero)
print(sequencia)



