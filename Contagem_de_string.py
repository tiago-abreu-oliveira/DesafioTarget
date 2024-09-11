# Solicitar ao usuário para digitar uma string
texto = input("Digite uma string: ")

# Inicializar a contagem
contagem = 0

# Verificar cada caractere da string
for char in texto:
    # Verificar se o caractere é 'a' ou 'A'
    if char == 'a' or char == 'A':
        contagem += 1

# Verificar se a contagem é maior que 0 e exibir a mensagem apropriada
if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
