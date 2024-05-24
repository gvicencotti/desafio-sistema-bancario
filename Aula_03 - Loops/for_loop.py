texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end ="")

print()

