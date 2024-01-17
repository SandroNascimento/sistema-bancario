saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = """
    Menu:
    d - Deposito
    s - Saque
    e - Extrato
    q - Sair

    Escolha a operação desejada: """

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: +R$ {valor_deposito:.2f}\n"
        else:
            print("Operação Falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numeros_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: R$ "))
            if valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                extrato += f"Saque: -R$ {valor_saque:.2f}\n"
                numeros_saques += 1
            else:
                print("Saldo insuficiente ou limite de saque excedido.")
        else:
            print("Limite diário de saques atingido.")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print("===================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")