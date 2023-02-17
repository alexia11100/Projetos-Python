def user_main(usuario):
    def depositar(saldo,valor,extrato):
        if valor > 0:
            saldo += valor
            extrato += f"+R$ {valor:.2f}\n"
            return saldo,extrato

        else:
            return []

    def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
        if (0 < valor <= limite) and (saldo >= valor) and (numero_saques < limite_saques):
            saldo -= valor
            extrato += f"-R$ {valor:.2f}\n"
            return [saldo,extrato]

        else:
            return []

    def ver_extrato(saldo,/,extrato):
        if extrato:
            print("Extrato")
            print(extrato + f"\nSaldo Atual: R$ {saldo:.2f}")

        else:
            print("Extrato")
            print("Não foram realizadas movimentações.")

            if saldo:
                print(f"\nSaldo Atual: R$ {saldo:.2f}")

    saldo = usuario["saldo"]
    extrato = ""
    LIMITE = usuario["limite"]
    numero_saques = usuario["numero_saques"]
    LIMITE_SAQUES = usuario["limite_saques"]

    menu = f"""Bem-vindo {usuario["nome"]}


    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            print("Depósito")
            valor = float(input("Valor: "))
            deposito = depositar(saldo,valor,extrato)

            if len(deposito) == 2:
                saldo, extrato = deposito[0], deposito[1]
                usuario["saldo"] = saldo
                print("Depósito efetuado com sucesso.")

            else:
                print("Algo deu errado, siga os passos abaixo:")
                print("1) Efetue apenas depósitos positivos maiores que 0.")

        elif opcao == "s":
            print("Saque")
            valor = float(input("Valor: "))
            saque = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=LIMITE,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)

            if len(saque) == 2:
                saldo, extrato = saque[0], saque[1]
                numero_saques += 1
                usuario["saldo"] = saldo
                usuario["numero_saques"] = numero_saques
                print("Saque efetuado com sucesso.")

            else:
                print("Algo deu errado, siga os passos abaixo:")
                print("1) Verifique se o valor de saque está dentro do limite permitido de 'R$0.01' a 'R$500.00'.")
                print("2) Verifique se você tem saldo o suficiente na conta.")
                print("3) Se não for nada disso, significa que você excedeu seu número de saques por dia.")

        elif opcao == "e":
            ver_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação Inválida, por favor tente novamente.")

def main():
    def criar_usuario(*,nome,senha,usuarios):
        if len(usuarios) > 0:
            contas = [int(usuario["conta"]) for usuario in usuarios]
            contas.sort()
            conta = str(max(contas) + 1)

        else:
            conta = str(1)

        usuario = {"nome": nome,
                   "conta": conta,
                   "senha": senha,
                   "saldo": 0,
                   "limite": 500,
                   "numero_saques": 0,
                   "limite_saques": 3
                   }
        return usuario

    def valida_login(*,conta,senha,usuarios):
        if len(usuarios) > 0:
            for usuario in usuarios:
                if usuario["conta"] == conta:
                    if usuario["senha"] == senha:
                        return usuario

            return False

        else:
            return False

    usuarios = []
    menu = """

    [e] Entrar
    [c] Criar Conta
    [q] Sair

    => """
    while True:
        opcao = input(menu).lower()

        if opcao == "e":
            conta = input("Conta Corrente: ")
            senha = input("Senha: ")
            usuario = valida_login(conta=conta,senha=senha,usuarios=usuarios)

            if usuario:
                user_main(usuario)

            else:
                print("Algo deu errado, siga os passos abaixo:")
                print("1) Sua conta não existe.")
                print("2) Sua senha está incorreta.")

        elif opcao == "c":
            nome = input("Nome: ")
            senha = input("Senha: ")
            usuario = criar_usuario(nome=nome,senha=senha,usuarios=usuarios)
            usuarios.append(usuario)
            print("Conta criada com sucesso, confira seus dados:")
            print(f"Nome: {usuario['nome']}")
            print(f"Conta: {usuario['conta']}")
            print(f"Senha: {usuario['senha']}")

        elif opcao == "q":
            break

        else:
            print("Operação Inválida, por favor tente novamente.")

main()
