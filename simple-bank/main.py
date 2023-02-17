menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")

        valor = float(input("Valor: "))
        if valor > 0:
            saldo += valor
            extrato += f"+R$ {valor:.2f}\n"

    elif opcao == "s":
        print("Saque")

        valor = float(input("Valor: "))
        if (0 < valor <= 500) and (saldo >= valor) and (numero_saques < LIMITE_SAQUES):
            saldo -= valor
            extrato += f"-R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Algo deu errado, siga os passos abaixo:")
            print("1) Verifique se o valor de saque está dentro do limite permitido 'R$500.00'")
            print("2) Verifique se você tem saldo o suficiente na conta")
            print("3) Se não for nada disso, significa que você excedeu seu número de saques por dia")

    elif opcao == "e":
        if extrato:
            print("Extrato")
            print(extrato+f"\nSaldo Atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor tente novamente.")
