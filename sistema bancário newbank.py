class Conta:
    def __init__(self, numero, titular, saldo=0, limite=15000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self.saldo -= valor
            conta_destino.depositar(valor)
            self.extrato.append(f"Transferência enviada: R$ {valor:.2f} para conta {conta_destino.numero}")
            print(f"Transferência de R$ {valor:.2f} para a conta {conta_destino.numero} realizada com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n________________EXTRATO__________________")
        print("Não foram realizadas movimentações." if not self.extrato else "\n".join(self.extrato))
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("___________________________________________")


def main():
    contas = {}

    while True:
        menu = """
        [c] Criar Conta
        [d] Depositar
        [p] Pix
        [s] Sacar
        [t] Transferir
        [e] Extrato
        [q] Sair
        [I] Internetbank

        => """
        
        opcao = input(menu)

        if opcao == "c":
            numero = input("Informe o número da conta: ")
            titular = input("Informe o nome do titular da conta: ")
            contas[numero] = Conta(numero, titular)
            print(f"Conta {numero} criada com sucesso para {titular}!")

        elif opcao == "d":
            numero = input("Informe o número da conta: ")
            if numero in contas:
                valor = float(input("Informe o valor do depósito: "))
                contas[numero].depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "s":
            numero = input("Informe o número da conta: ")
            if numero in contas:
                valor = float(input("Informe o valor do saque: "))
                contas[numero].sacar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao == "t":
            numero_origem = input("Informe o número da conta de origem: ")
            numero_destino = input("Informe o número da conta de destino: ")
            if numero_origem in contas and numero_destino in contas:
                valor = float(input("Informe o valor da transferência: "))
                contas[numero_origem].transferir(valor, contas[numero_destino])
            else:
                print("Conta de origem ou destino não encontrada.")

        elif opcao == "e":
            numero = input("Informe o número da conta: ")
            if numero in contas:
                contas[numero].exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()

