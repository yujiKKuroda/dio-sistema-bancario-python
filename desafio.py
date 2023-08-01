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

    opcao = input(menu)

    if opcao == "d":
        while True: 
            deposito = input("Quanto você quer depositar?\n=> ")
            if float(deposito) > 0:
                saldo += float(deposito)
                extrato += """
                Depósito = +R${deposito:.2f}
                """
                print("Depósito bem-sucedido!")
                break
            else:
                print("Valor inválido, por favor tente novamente!")

    elif opcao == "s":
        print("Saque")

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
