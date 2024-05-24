curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # Mesma ocupação de memória entre o objeto A e objeto B
curso is not nome_curso  # Diferente ocupação de memória entre o objeto A e objeto B
saldo is limite # Exemplo com valores inteiros

saldo = 1000
limite = 500

print(saldo is limite) #False
print(saldo is not limite) #True