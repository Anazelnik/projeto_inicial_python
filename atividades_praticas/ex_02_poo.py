class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.'
    
pessoa_1 = Pessoa('Ana', 28, 'Engenheira')
pessoa_2 = Pessoa('Bruno', 35, 'Médico')
pessoa_3 = Pessoa('Carla', 22, 'Designer')

print("Informações iniciais:")
print(pessoa_1)
print(pessoa_2)
print(pessoa_3)

pessoa_1.aniversario()
pessoa_3.aniversario()

print("\nApós aniversários:")
print(pessoa_1.saudacao)
print(pessoa_2.saudacao)
print(pessoa_3.saudacao)


# EX - 01
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Conta de {self.titular} | Saldo: R$ {self._saldo}'
    
    def ativar_conta(self):
        self.ativo = True

conta_1 = ContaBancaria('Ana', 1500.00)
conta_2 = ContaBancaria('Bruno', 3000.00)
print(conta_1)
print(conta_2)

conta_3 = ContaBancaria('Carla', 500.00)
conta_3.ativar_conta()
print(f'Depois de ativar: Conta ativa? {conta_3.ativo}')

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True

# EX - 02 
class ClienteBanco:
    def __init__(self, nome, idade, profissao, saldo, agencia):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.saldo = saldo
        self.agencia = agencia

    def __str__(self):
        return print(f'Cliente: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}, Saldo: R$ {self.saldo:.2f}, Agência: {self.agencia}')
    
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta

cliente_1 = ClienteBanco('Ana', 28, 'Engenheira', 2500.00, '001')
cliente_2 = ClienteBanco('Bruno', 35, 'Médico', 5000.00, '002')

conta_cliente1 = ClienteBanco.criar_conta('Marcela', 3000.00)
print(f'Conta criada para {conta_cliente1.titular} com saldo inicial de R$ {conta_cliente1.saldo:.2f}')