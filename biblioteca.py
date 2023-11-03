# Conta Bancária
class contaBancaria:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0

    def ativarConta(self):
        if self.status == False:
            self.status = True
            print("Sua conta foi ativada com sucesso!")
        else:
            print("Sua conta já está ativa!")
    def desativarConta(self):
        if self.status == True:
            self.status = False
            print("Sua conta foi desativada com sucesso!")
        else:
            print("Sua conta já está desativada.")
    def depositar(self, valor):
        if self.status == True:
            self.saldo = self.saldo + valor
            print(f"Depósito feito com sucesso! Seu saldo é de R${self.saldo}")
        else:
            print("Sua conta está desativada! Ative primeiro sua conta para prosseguir com a operação.")
    def sacar(self, valor_saque):
        if self.status == True:
            if valor_saque > 0 and valor_saque <= self.saldo:
                self.saldo = self.saldo - valor_saque
                print(f"Saque realizado com sucesso! Seu saldo é de R${self.saldo}")
            elif valor_saque > self.saldo and self.limite > 0:
                self.limite = self.limite - (valor_saque - self.saldo)
                print(f"Saque realizado com sucesso! Seu saldo é de R${self.limite}")
            else:
                print("Não foi possível fazer o saque, pois sua conta está zerada ou negativa.")
        else:
            print("Sua conta está desativada! Ative primeiro sua conta para fazer o saque.")
    def verificarSaldo(self):
        if self.status == True:
            print(f"Seu saldo é de {self.saldo}.")
        else:
            print("Sua conta está desativada. Primeiro ative sua conta para prosseguir com a operação.")
    def ativarLimite(self, limite):
        if self.status == True:
            self.limite = limite
            self.saldo = self.saldo + limite
            print(f"Seu saldo com limite de crédito é de R${self.saldo}")
        else:
            print("Sua conta está desativada.")

# Classe do Jogo Tamagotchi
class Tamagotchi:
    def __init__(self, bichinho, nome):
        self.bichinho = bichinho
        self.nome = nome
        self.comendo = False
        self.banheiro = False
        self.brincando = False
        self.vacina = False
    def comer(self, comida):
        if self.comendo == True:
            print(f"{self.nome} já está comendo.")
        else:
            print(f"{self.nome} começou a comer {comida}")
            self.comendo = True
    def pararComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} não estava comendo.")
    def foiBanheiro(self):
        if self.banheiro == True:
            print(f"{self.nome} já está no banheiro.")
        else:
            print(f"{self.nome} foi ao banheiro.")
            self.banheiro = True
    def saiuBanheiro(self):
        if self.banheiro == True:
            print(f"{self.nome} saiu do banheiro.")
            self.banheiro = False
        else:
            print(f"{self.nome} não está no banheiro.")
    def brincar(self):
        if self.brincando == True:
            print(f"{self.nome} já está brincando.")
        else:
            print(f"{self.nome} começou a brincar.")
            self.brincando = True

    def pararBrincar(self):
        if  self.brincando == True:
            print(f"{self.nome} parou de brincar.")
            self.brincando = False
        else:
            print(f"{self.nome} não está brincando.")
    def curar(self):
        if self.vacina == True:
            print(f"{self.nome} já tomou vacina.")
            self.vacina = True
        else:
            print(f"{self.nome} foi tomar vacina.")

# Herança animal
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self, comida):
        print(f"O {self.nome} foi comer {comida}.")

    def emitirSom(self):
        print(f"O {self.nome} está emitindo um som.")

    def dormir(self):
        print(f"O {self.nome} está dormindo.")
class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"A {self.nome} está mugindo")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f'O {self.nome} está latindo.')
class Coelho(Animal):
    def __init__(self, nome, cor):
        super(). __init__(nome, cor)
    def emitirSom(self):
        print(f"O {self.nome} está chiando.")
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"O {self.nome} está miando.")
class Calopsita(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f"A {self.nome} está cantando.")


