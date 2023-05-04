"""
1)	Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os códigos de dez
contas e os seus respectivos saldos. Os códigos devem ser armazenados em um vetor de números inteiros (não pode haver
mais que uma conta com o mesmo código) e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá
ser cadastrado na mesma posição do código. Por exemplo, se a conta 504 for armazenada na quinta posição do vetor de
saldos. Depois de fazer a leitura dos valores, mostrar o seguinte menu na tela:
1.	Efetuar depósito
2.	Efetuar saque
3.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
4.	Finalizar o programa
Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não estiver cadastrada,
 mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, atualizar o seu saldo.
Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada,
mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, verificar se o seu saldo é suficiente
para cobrir o saque. (Estamos supondo que a conta não pode ficar com o saldo negativo). Se o saldo for suficiente,
realizar o saque e voltar ao menu. Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.
Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor,
voltar ao menu.
O programa só termina quando for digitada a opção 4 – Finalizar o programa.
"""
# Criação das listas vazias para armazenar os códigos e saldos das contas bancárias
contas = [0] * 10 # lista para armazenar os códigos das contas
saldos = [0] * 10

#Loop para cadastrar as contas
for c in range(10):
    repete = True
    while repete:
        print("Digite o numero da conta")
        numero = int(input())
        i = 0
        # Verifica se o código já existe na lista
        while i < 10:
            if numero == contas[i]:
                print("Conta duplicada")
                break
            i = i + 1
        if i == 10:
            print("Conta cadastrada")
            contas[c] = numero
            repete = False
    print("Digite o saldo")
    saldos[c] = int(input())
# Exibe o menu de opções
opcao = 0
while opcao != 4:
    print("Menu")
    print("1.	Efetuar depósito")
    print("2.	Efetuar saque")
    print("3.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)")
    print("4.	Finalizar o programa")
    print("Digite a opcao")
    opcao = int(input())
    # Opção 1: Efetuar depósito
    if opcao == 1:
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do deposito")
        valdep = float(input())
        i = 0
        while i < 10:
            if numero == contas[i]:
                print("Conta encontrada")
                saldos[i] = saldos[i] + valdep
                break
            i = i + 1
        if i == 10:
            print("Conta nao encontrada")
    # Opção 2: Efetuar saque
    if opcao == 2:
        print("Digite o numero da conta")
        numero = int(input())
        print("Digite o valor do saque")
        valsaq = float(input())
        i = 0
        while i < 10:
            if numero == contas[i]:
                print("Conta encontrada")
                if saldos[i] >= valsaq:
                    saldos[i] = saldos[i] - valsaq
                else:
                    print(f"saldo insuficiente - saldo {saldos[i]}")
                break
            i = i + 1
        if i == 10:
            print("Conta nao encontrada")
    # Opção 3: Consultar o ativo bancário
    if opcao == 3:
        total = 0
        for i in range(10):
            print(f"Conta {contas[i]} saldo {saldos[i]}")
            total = total + saldos[i]
        print("O total e ", total)
