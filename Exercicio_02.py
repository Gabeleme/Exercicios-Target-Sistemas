texto = input("Digite uma palavra: ")

total_a = 0

# Percorre cada caractere da string
for char in texto:
    if char == 'a' or char == 'A':
        total_a += 1

if total_a > 0:
    print(f"A letra 'a/A' aparece {total_a} vezes na string.")
else:
    print("A letra 'a/A' não está presente na string.")
