from time import sleep


class ContaBancaria:
    def __init__(self, titular_conta, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("Saldo inválido")

        self.titular = titular_conta
        self.__saldo = saldo_inicial
        self.historico_da_conta = []

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self,valor):
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")

        self.__saldo += valor
        self.historico_da_conta.append(f"Depósito: +{valor}")

    def sacar(self,valor):
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        elif valor > self.__saldo:
            raise ValueError("Saldo insuficiente")

        self.__saldo -= valor
        self.historico_da_conta.append(f"Saque: -{valor}")

    def status_account(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"

    def ver_historico(self):
        if not self.historico_da_conta:
            return "Sem movimentações"

        return "\n".join(self.historico_da_conta)

if __name__ == "__main__":
    print("\033[34m=\033[m" * 30)
    print('\033[92mCONTROLE DE SISTEMA BANCARIO\033[m')
    print("\033[34m=\033[m"*30)

    print("")
    titular = input("Titular: ")
    saldo = float(input("Saldo Inicial: "))
    conta_titular = ContaBancaria(titular,saldo)

    while True:
        print("\n" + "=" * 30)
        print("[1] - Mostrar Status da Conta")
        print("[2] - Depositar")
        print("[3] - Sacar")
        print("[4] - Ver Historico")
        print("[0] - Sair")
        print("=" * 30)

        try:
            opcao = int(input("Opção: "))
            match opcao:
                case 1:
                    print(conta_titular.status_account())

                case 2:
                    valor_deposito = float(input("Depositar: "))
                    conta_titular.depositar(valor_deposito)
                    print("Depósito realizado!")

                case 3:
                    valor_saque = float(input("Sacar: "))
                    conta_titular.sacar(valor_saque)
                    print("Saque realizado!")

                case 4:
                    print("Histórico")
                    print(conta_titular.ver_historico())

                case 0:
                    print("Saindo...")
                    sleep(1)
                    break

                case _:
                    print("Opção inválida")

        except ValueError as e:
                print(f"Erro: {e}")

    print("VOCÊ SAIU DO SISTEMA BANCARIO")
