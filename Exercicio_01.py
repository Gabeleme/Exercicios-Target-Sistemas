def pertence_fibonacci(numero):
    if numero < 0: # se for negativo não pode estar na sequencia
        return False
    
    a, b = 0, 1 #inicializando com esses valores
    
    while a <= numero: #gera a sequencia enquanto for menor que o informado
        if a == numero: # se o informado for igual 
            return True
        a, b = b, a + b #atualiza a sequencia com
    
    return False

numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci e imprime a mensagem 
if pertence_fibonacci(numero):
     print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
    