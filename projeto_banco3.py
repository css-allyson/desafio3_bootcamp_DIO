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
    def __init__(self, numero:int, cliente:Cliente, historico:Historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    @classmethod
    def nova_conta(cls,cliente:Cliente,numero:int):
        return cls(numero, cliente)
    
    def sacar(self,valor:float):
        saldo = self._saldo
        valor_indisponível = valor>self._limite
        if valor_indisponível:
            print("A conta não tem saldo suficiente para realizar o saque no valor desejado")
        elif valor > 0:
            self._saldo -=valor
            print("saque realizado com sucesso")
            return True
        else:
            print("Valor informado não é válido")

        return False
    def depositar(self,valor:float):
        if valor > 0:
            self._saldo+=valor
            print("Depósito realizado com sucesso")
            return True
        else:
            print("Valor informado não é válido")
            return False

class Cliente:
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas = []
    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self._contas.append(conta)



class ContaCorrente(Conta):
    def __init__(self, numero:int, cliente:Cliente, limite:float=500, limite_saques:int=3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques=limite_saques
    def sacar(self,valor:float):
        valor_indisponível = valor>self._limite
        superou_saques = len(self._historico._saques) >= self._limite_saques

        if valor_indisponível:
            print("A conta não tem saldo suficiente para realizar o saque no valor desejado")

        elif superou_saques:
            print("Número de saques diários excevido")

        else:
            return super().sacar(valor)



class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta):
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