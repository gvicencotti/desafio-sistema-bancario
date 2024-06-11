from abc import ABC, abstractmethod, abstractproperty

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas_correntes = []

class Conta:
    def __init__(self, saldo, numero_conta, agencia, cliente, historico):
        self._saldo=saldo
        self.numero_conta=numero_conta
        self.agencia=agencia
        self.cliente=cliente
        self.historico=historico

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
print(conta_1 = Conta(1, 2, AGENCIA, "Cleiton", "batata"))
        

# Declaração das variáveis e constantes


def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):

    if numero_saques == LIMITE_SAQUES:
        print("Você chegou ao seu limite de saques diários. Por gentileza, tente novamente amanhã.")
        print("\nDeseja realizar outra operação?")
        return saldo, extrato, numero_saques
    
    valor = float(input("\nValor a ser sacado: R$ "))

    if valor > limite:
        print(f"Você ultrapassou o limite de R${limite:.2f}, operação não autorizada. Gostaria de realizar outra operação?")
        return saldo, extrato, numero_saques


    if numero_saques >= limite_saques:
        print("Você excedeu o seu limite de saques diários. Por gentileza, tente novamente amanhã.")
        print("\nDeseja realizar outra operação?")
        return saldo, extrato, numero_saques
        

    if valor > saldo:
        print("Você não possui saldo o suficiente para completar a transação.")
        return saldo, extrato, numero_saques
        

    if valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print("=================================")
        print("\nDeseja realizar outra operação?")
    else:
        print("=================================")
        print("Não é possível concluir a operação. Retornando ao menu")

    return saldo, extrato, numero_saques
 
def depositar(saldo, valor, extrato, /):
    valor = float(input("\nValor a depositar: R$ "))

    if valor > 0:
        saldo += valor
        extrato += f" Depósito: R${valor:.2f}\n "
        print("=================================")
        print("\nDeseja realizar outra operação?")
    else:
        print("=================================")
        print("\nNão foi possível concluir a operação, retornando ao menu")
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    if extrato == "": 
        print("\nNão foram realizadas movimentações na conta!")
    else:
        print(extrato)
        print(f"Seu saldo é de R${saldo}!")  

def criar_usuario(): 
    print("=============== CADASTRO ==================\n")
    print("Por gentileza, informe seus dados abaixo para realizarmos seu cadastro.")
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF:")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)

    return nome, data_nascimento, cpf, endereco

def criar_conta_corrente(agencia, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    for usuario in usuarios:
        if  usuario['cpf'] == cpf:
            numero_conta = len(contas_correntes) + 1 #Geração do número da conta através da quantidade de contas criadas
            print("\nSua conta foi criada com sucesso!")
            conta_corrente = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
            contas_correntes.append(conta_corrente)
            return conta_corrente
        
    print("Não foi possível identificar o usuário.")
    return None # Criação de usuário não foi bem sucedida

def listar_contas(contas_correntes):
    if not contas_correntes:
        print("Não há contas correntes cadastradas.")
        return
    
    print("=== Contas Correntes ===")
    for conta in contas_correntes: # Itera sobre os dados das contas correntes e apresenta os dados
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print("Titular:")
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print("------------------------")

# Menu principal de exibição
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Listar Conta Corrente
[7] Sair

=> """

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        saldo, extrato = depositar(saldo, valor, extrato)     
    elif opcao == 2:
        saldo, extrato, numero_saques = sacar(saldo=saldo,
                                              extrato=extrato,
                                              limite=limite, 
                                              numero_saques=numero_saques, 
                                              limite_saques=LIMITE_SAQUES)
    elif opcao == 3:
        mostrar_extrato(saldo, extrato=extrato)
    elif opcao == 4:
        criar_usuario()
    elif opcao == 5:
        criar_conta_corrente(AGENCIA, usuarios)
    elif opcao == 6:
        listar_contas(contas_correntes)


    elif opcao == 7:
        print("Obrigado pela preferência aos nossos serviços!")
        break
    
    else:
        print("Opção inválida, retornando ao menu principal.")

