saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas_correntes = []

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("Você ultrapassou o limite de R$500.00, operação não autorizada. Gostaria de realizar outra operação?")
        return saldo, extrato, numero_saques


    if numero_saques == limite_saques:
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
    cpf = int(input("CPF:"))
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)

    return nome, data_nascimento, cpf, endereco

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")

    for usuario in usuarios:
        if str(usuario['cpf']) == cpf:
            print("\nSua conta foi criada com sucesso!")
            conta_corrente = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
            contas_correntes.append(conta_corrente)
            return conta_corrente
        
    print("Não foi possível identificar o usuário.")
    return None

def listar_contas(contas_correntes):
    if not contas_correntes:
        print("Não há contas correntes cadastradas.")
        return
    
    print("=== Contas Correntes ===")
    for i, conta in enumerate(contas_correntes, start=1):
        usuario = conta["usuario"]
        print(f"Conta {i}:")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print("Titular:")
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['cpf']}")
        print("------------------------")

numero_conta = len(usuarios) + 1

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
        valor = float(input("\nValor a depositar: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)
        
    
    elif opcao == 2:
        valor = float(input("\nValor a ser sacado: R$ "))
        saldo, extrato, numero_saques = sacar(saldo=saldo,
                                            valor=valor,
                                            extrato=extrato,
                                            limite=limite, 
                                            numero_saques=numero_saques, 
                                            limite_saques=LIMITE_SAQUES)

    elif opcao == 3:
        mostrar_extrato(saldo, extrato)

    elif opcao == 4:
        criar_usuario()

    elif opcao == 5:
        criar_conta_corrente(AGENCIA, numero_conta, usuarios)
        numero_conta += 1

    elif opcao == 6:
        listar_contas(contas_correntes)


    elif opcao == 7:
        print("Obrigado pela preferência aos nossos serviços!")
        break
    
    else:
        print("Opção inválida, retornando ao menu principal.")

