while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break # quebra o looping

    if numero % 2 == 0:
        continue # pula a execução do código e vai para a próxima instrução
    
    print(numero)