saldo = 0
LIMITE_SAQUES = 3
numero_saques = 0
limite = 500
extrato = ""
    
    
while True:
    
    menu = input("""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a opção desejada:

""")
        
    if menu == "d":
        
        deposito = int(input("Digite o valor a ser depositado: "))
        
        if deposito > 0:
            
            saldo += deposito
            extrato += f"Depósito de R${deposito:.2f}\n"
            
        else:
            print("Valor digitado inválido.")
        
    elif menu == "s":
        valor = int(input("Digite o valor que deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor > limite
        
        if excedeu_saldo:
            print("Valor indisponível.")
        elif excedeu_saques:
            print("Limite de saques diários ultrapassado.")
        elif excedeu_limite:
            print("Limite máximo por saque: R$500")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Valor digitado inválido.")
    
    elif menu == "e":
        print("Não houve movimentação" if not extrato else extrato)
        print(f"Sando total em conta R${saldo:.2f}.")
    
    elif menu == "q":
        break
    
    else:
        print("Opção Inválida.")
        
    
    
    