opcao =-1
saldo = 0
extrato = ""
LIMITE_SAQUE=500
LIMITE_SAQUE_DIARIO=0


while opcao != 0:
    opcao=int(input("[1]Sacar\n[2]Depositar\n[3]Extrato\n[0]Sair\n=>"))
#opção de saque
    if opcao == 1:
        print("\n================ SAQUE ================")
        if LIMITE_SAQUE_DIARIO >=3:
            print("Limite de saque diario excedido!")
            break
        saque=int(input("Qual valor você quer sacar?\n=>R$"))
        if saque <= saldo:
            saldo = saldo - saque
            if saque <= 500:
                 print ("\nRetire seu dinheiro na boca do caixa!\n")
                 print(f"Seu saldo agora é de:R$ {saldo}\n")
                 extrato += f"Saque: R$ {saldo:.2f}\n"
                 LIMITE_SAQUE_DIARIO+=1
            if saque >=501:
                print (f"\nValor de saque excedido!\nValor maximo para saque é de: R${LIMITE_SAQUE}")
                break
        else:
            print("Saldo insuficiente.\n")
        print("==========================================")

#opção de deposito
    if opcao == 2:
        print("\n================ DEPOSITO ================")
        deposito=int(input("Qual valor você deseja depositar?\n=>R$"))
        if deposito <=0:
            print("Não foi possivel realizar essa operação!(Valor invalido).\n")
        else:
            print(f"valor depositado de:R$ {deposito}\n")        
            saldo= saldo + deposito
            extrato += f"Depósito: R$ {saldo:.2f}\n"

#opção de extrato
    if opcao == 3:
          print("\n================ EXTRATO ================")
          print("Não foram realizadas movimentações." if not extrato else extrato)
          print(f"\nSaldo: R$ {saldo:.2f}")
          print("==========================================")

print("Obrigado por usar nosso sistema bancario, Até Logo ❤️")