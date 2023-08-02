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
            deposito_float = float(deposito)
            if deposito_float > 0:
                saldo += deposito_float
                extrato += f"Depósito = +R${deposito_float:.2f}\n"
                print("Depósito bem-sucedido!")
                break
            else:
                print("Valor inválido, por favor tente novamente!")

    elif opcao == "s":
        while True:
            if numero_saques <= LIMITE_SAQUES:
                saque = input("Quanto você quer sacar?\n=> ")
                saque_float = float(saque)

                if saque_float > limite:
                    print("Valor muito alto, máximo de R$500.00 por transação! Por favor tente novamente!")
                elif saque_float > 0:
                    if (saque_float <= saldo):
                        saldo -= saque_float
                        extrato += f"Saque = +R${saque_float:.2f}\n"
                        print("Saque bem-sucedido!")
                        break
                    else:
                        print("Saldo insuficiente, tente novamente!")
                else:
                    print("Valor inválido, por favor tente novamente!")
            else:
                print("Você alcançou o máximo de saques hoje, não tente novamente!")
                break

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
