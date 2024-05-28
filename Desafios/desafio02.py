menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        
        valor = float(input("\nValor a depositar: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f" Depósito: R${valor:.2f}\n "
            print("=================================")
            print("\nDeseja realizar outra operação?")
        else:
            print("=================================")
            print("\nNão foi possível concluir a operação, retornando ao menu")
    
    elif opcao == 2:

        if numero_saques == LIMITE_SAQUES:
            print("Você chegou ao seu limite de saques diários. Por gentileza, tente novamente amanhã.")
            print("\nDeseja realizar outra operação?")
            continue
        
        valor = float(input("\nValor a ser sacado: R$ "))

        if valor > saldo:
            print("Você não possui saldo o suficiente para completar a transação.")
        elif valor > 500:
            print("Você não possui limite o suficiente para completar a transação.")
        

        if valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
            print("=================================")
            print("\nDeseja realizar outra operação?")
        else:
            print("=================================")
            print("Não é possível concluir a operação. Retornando ao menu")

    elif opcao == 3:
        if extrato == "": 
            print("\nNão foram realizadas movimentações na conta!")
        else:
            print(extrato)
            print(f"Seu saldo é de R${saldo}!")
    
    elif opcao == 4:
        print("Obrigado pela preferência aos nossos serviços!")
        break
    
    else:
        print("Opção inválida, retornando ao menu principal.")