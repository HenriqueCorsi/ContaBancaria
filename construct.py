class Conta_bancaria:
    def __init__(self, numero_conta, titular_conta, saldo_conta, limite_conta):
        # Definido os Parametros e tornando todos eles privados
        self.__numero_conta = numero_conta
        self.__titular_conta = titular_conta
        self.__saldo_conta = saldo_conta
        self.__limite_conta = limite_conta

    # Método que exibi o extrato da conta
    def exibir_extrato(self):
        print('\n----------------EXTRATO-------------------')
        print(f'Saldo ->           R${self.__saldo_conta}')
        print(f'Limite Disponovel  R${self.__limite_conta}')
        print(f'Títular ->         {self.__titular_conta}')
        print(f'Númeor da conta -> {self.__numero_conta}')

    # Método que realiza o saque de valores da conta
    def saque(self, valor_saque):
        if valor_saque <= self.__saldo_conta + self.__limite_conta:
            self.__saldo_conta = self.__saldo_conta - valor_saque
        else:
            print('Saldo Indisponivel.')

    # Método que recebe depositos
    def depositar(self, valor_deposito):
        self.__saldo_conta = self.__saldo_conta + valor_deposito

    # Método que realiza transferencia de valores de um objeto para o outro
    def pix(self, valor, destinatario):
        if valor <= self.__saldo_conta + self.__limite_conta:
            print(f'\nTransferencia de R$ {valor} realizada com sucesso.')
            destinatario.depositar(valor)
        else:
            print('\nSaldo Indisponivel para pix.')

    # Método que altera o saldo caso seja necessario
    def set_saldo(self, novo_saldo):
        self.__saldo_conta = novo_saldo

    # Método que altera o limite caso seja necessario
    def set_limite(self, novo_limite):
        self.__limite_conta = novo_limite
        # Método estatico (que já pertence a classe) exibi o código do banco

    @staticmethod
    def codigo_banco():  # Este método por ser estático, pode ser chamado sem a necessidade de um objeto
        return '555'


