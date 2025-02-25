texto = 'Banco do Marlinho'.upper()
largura_texto = 20
enchimento_texto = '-'
contador_depositos = 0
limite_saques = 3
valor_limite_saque = 500 
contador_saques = 0 
saldo = 0 
extrato = []
print('=-=' * 20)
print(texto.center(60,'-'))
print('=-=' * 20)
print('')
print('Digite a Operação desejada: ')
print('')
print('[ 1 ] Depositar')
print('[ 2 ] Sacar ')
print('[ 3 ] Extrato ')
print('[ 4 ] Sair ')
print('')


while True:
    
    operacao = int(input('Digite a operação desejada: '))

    if operacao == 1:
       while True:
           valor_deposito = float(input('Digite o valor a ser depositado: '))
           print(f'Depósito de {valor_deposito} feito com sucesso!')
           if valor_deposito < 0:
               print('Valor inválido! o número não pode ser negativo. Tente novamente!')
           else:
               saldo += valor_deposito
               contador_depositos += 1
               extrato.append(f'\033[32mDepósito: R${valor_deposito:.2f}\033[0m')
               break   
    elif operacao == 2:
        if contador_saques >= limite_saques:
            print('Você já atingiu o limite de saques diários. Tente novamente amanhã.')
        else:
            valor_saque = float(input('Digite o valor que deseja sacar: '))
            if valor_saque > saldo:
                print(f'Não é possível realizar o saque pois não há saldo suficiente na conta.')
            elif valor_saque > valor_limite_saque:
                print('Não é possível sacar esse valor, pois ultrapassa o limite de saque.')
            else:
                saldo -= valor_saque
                extrato.append(f'\033[31mSaque: R${valor_saque:.2f}\033[0m')
                contador_saques += 1
                print(f'Saque de R${valor_saque:.2f} realizado com sucesso!')
    elif operacao == 3:
        print('Extrato de Conta:')
        if not extrato:
            print('Não houve transações realizadas')
        else:
            for transacao in extrato:
                print(transacao)
        print(f'\033[34mSaldo atual da conta: R${saldo:.2f}\033[0m')            

    elif operacao == 4:
        print('Desligando sistema.. até mais tarde!')
        break
    else:
        print('Escolha inválida, tente novamente!')    




