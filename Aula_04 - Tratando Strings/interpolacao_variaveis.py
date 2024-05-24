nome = "Gustavo"
idade = 30
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade,trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))
print("Olá, me chamo {}. Eu tenho {} anos de idade,trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade,trabalho como {1} e estou matriculado no curso de {0}".format(nome, idade, profissao, linguagem))
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade,trabalho como {profissao} e estou matriculado no curso de {linguagem}")


PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # 2 casas após a vírgula
print(f"Valor de PI: {PI:10.2f}") # 10 espaços e 2 casas após a vírgula