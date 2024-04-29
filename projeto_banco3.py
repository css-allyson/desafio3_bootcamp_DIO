from abc import ABC, abstractmethod

class Historico:
    def __init__(self, depositos:list, saques:list):
        self._depositos=[]
        self._saques=[]
    def adicionar_transacao(self,transacao:Transacao):
        if transacao.__class__.__name__ == Deposito:
            self.depositos.append(transacao)
        else:
            self.saques.append(transacao)


class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    def saldo(self):
        return self._saldo
    def nova_conta(self,cliente:Cliente,numero:int):
        self._
    pass
class Cliente:
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas = []
    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self._contas.append(conta)
class ContaCorrente(Conta):
    def __init__(self):
        pass
    pass

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta):
        pass
    pass

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self,conta:Conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta:Conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class PessoaFisica(Cliente):
    def __init__(self,nome:str, data_nascimento:str, cpf:str,endereco:str):
        super().__init__(endereco)
        self._nome=nome
        self._data_nascimento=data_nascimento
        self._cpf=cpf