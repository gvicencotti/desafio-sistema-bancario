from abc import ABC, abstractmethod
from datetime import datetime
import functools

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nome_funcao = func.__name__
        argumentos = f"args: {args}, kwargs: {kwargs}"
        valor_retornado = func(*args, **kwargs)
        entrada_log = f"{data_hora} - {nome_funcao} - {argumentos} - Retorno: {valor_retornado}\n"
        
        with open("log.txt", "a") as log_file:
            log_file.write(entrada_log)
        
        return valor_retornado
    
    return wrapper

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "descricao": transacao,
            "data_hora": datetime.now()
        })

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._numero_transacoes = 0
        self._data_ultima_transacao = datetime.min

    @classmethod
    def criar_nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def _atualizar_contagem_transacoes(self):
        hoje = datetime.now()
        if hoje.date() != self._data_ultima_transacao.date():
            self._numero_transacoes = 0
        self._data_ultima_transacao = hoje

    def verificar_limite_transacoes(self):
        self._atualizar_contagem_transacoes()
        if self._numero_transacoes >= 10:
            print("Você atingiu o limite diário de 10 transações.")
            return False
        return True

    @log_decorator
    def sacar(self, valor):
        self._atualizar_contagem_transacoes()
        if not self.verificar_limite_transacoes():
            return False

        if valor > self._saldo:
            print("Você não possui saldo o suficiente para completar a transação.")
            return False

        if valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao(f"Saque: R${valor:.2f}")
            self._numero_transacoes += 1
            print("==== Saque realizado com sucesso. ====")
            return True
        else:
            print("Não é possível concluir a operação.")
            return False
    
    @log_decorator
    def depositar(self, valor):
        self._atualizar_contagem_transacoes()
        if not self.verificar_limite_transacoes():
            return False

        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito: R${valor:.2f}")
            self._numero_transacoes += 1
            print("==== Depósito realizado com sucesso! ====")
            return True
        else:
            print("\nSaldo negativo. Não é possível concluir a transação.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    @log_decorator
    def sacar(self, valor):    
        self._atualizar_contagem_transacoes()
        if not self.verificar_limite_transacoes():
            return False

        if valor > (self._saldo + self._limite):
            print("Você ultrapassou o limite de saque disponível. Operação não autorizada.")
            return False      
        
        return super().sacar(valor)

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @log_decorator
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(f"Saque: R${self.valor:.2f}")

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @log_decorator
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(f"Depósito: R${self.valor:.2f}")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Listar Conta Corrente
[7] Sair
=> """

clientes = []
contas_correntes = []

def encontrar_conta(numero_conta):
    for conta in contas_correntes:
        if conta.numero == numero_conta:
            return conta
    return None

def encontrar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

@log_decorator
def depositar():
    numero_conta = input("Número da conta: ")
    valor = input("Valor do depósito: R$ ")
    
    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido.")
        return False
    
    conta = encontrar_conta(numero_conta)
    if conta:
        deposito = Deposito(valor)
        deposito.registrar(conta)
        return True
    else:
        print("Conta não encontrada.")
        return False

@log_decorator
def sacar():
    numero_conta = input("Número da conta: ")
    valor = input("Valor do saque: R$ ")
    
    try:
        valor = float(valor)
    except ValueError:
        print("Valor inválido.")
        return False
    
    conta = encontrar_conta(numero_conta)
    if conta:
        saque = Saque(valor)
        saque.registrar(conta)
        return True
    else:
        print("Conta não encontrada.")
        return False

@log_decorator
def mostrar_extrato():
    numero_conta = input("Número da conta: ")
    
    conta = encontrar_conta(numero_conta)
    if conta:
        print("==== Extrato ====")
        for transacao in conta.historico.transacoes:
            data_hora = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
            print(f"{data_hora} - {transacao['descricao']}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        return True
    else:
        print("Conta não encontrada.")
        return False

@log_decorator
def criar_usuario():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    
    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("Usuário criado com sucesso!")
    return True

@log_decorator
def criar_conta_corrente():
    cpf = input("CPF do cliente: ")
    cliente = encontrar_cliente(cpf)
    
    if cliente:
        numero = input("Número da conta: ")
        conta = ContaCorrente(numero, cliente)
        cliente.adicionar_conta(conta)
        contas_correntes.append(conta)
        print("Conta corrente criada com sucesso!")
        return True
    else:
        print("Cliente não encontrado.")
        return False

@log_decorator
def listar_contas():
    if contas_correntes:
        print("==== Contas Correntes ====")
        for conta in contas_correntes:
            print(f"Conta {conta.numero} - Saldo: R$ {conta.saldo:.2f}")
        return True
    else:
        print("Nenhuma conta corrente encontrada.")
        return False

while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        print("Opção inválida, retornando ao menu principal.")
        continue

    if opcao == 1:
        depositar()     
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        mostrar_extrato()
    elif opcao == 4:
        criar_usuario()
    elif opcao == 5:
        criar_conta_corrente()
    elif opcao == 6:
        listar_contas()
    elif opcao == 7:
        print("Obrigado pela preferência aos nossos serviços!")
        break
    else:
        print("Opção inválida, retornando ao menu principal.")
