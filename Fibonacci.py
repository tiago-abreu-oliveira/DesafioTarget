def pertence_a_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Solicitar entrada do usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verificar e exibir o resultado
if pertence_a_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
