class conta:
    #construtor
    def __init__(self, numero, titular, saldo, limite):
        print(self)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #funções da conta
    def extrato(self):
        print("O saldo é {} do titulas {}".format(self.__saldo, self.__titular))
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("ERROR: valor passou do limite")
    def transferir(self, destinatario, valor):
        self.sacar(valor)
        destinatario.depositar(valor)

    #métodos privados
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    #getters e setters
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_dos_bancos():
        return {"BB": "001"}
