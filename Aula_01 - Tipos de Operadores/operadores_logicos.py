print(True and True) # True
print(True and False) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or False or False) # False

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite) # Operador "and". Todos as comparações precisam ser verdadeiras
print(saldo >= saque or saque <= limite) # Operar "or". Alguma das comparações precisa ser verdadeira
print(not saldo < saque) # Operador "not". Apresenta o inverso

