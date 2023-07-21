#Codigo: Desafio DIO 2# Criando um sistema bancario com Python 
import textwrap #O módulo para quebra automática e formatação de texto simples

#Função das opções do MENU
def menu():
    menu = """\n
    ================MENU=================
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNovo usuário
        [5]\tNova Conta
        [6]\tListar Contas
        [0]\tSair
    =====================================
    """
    return input(textwrap.dedent(menu))

#Função de DEPOSITO: Recebe 'Positonal Only'
def depositar(saldo, valor, extrato, /):

    #Entradda de Valor
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n### Depósito realizado com sucesso! ###")
    #Erro de Entrada
    else:
        print("\n### Operação falhou! O valor informado é inválido. ###")

    return saldo, extrato

#Função de SAQUE: Recebe 'Keyword Only'
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    #Entradda de Valor
    if valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
    #Exedeu o Saldo
    elif valor > saldo: 
            print("### Operação falhou! Você não tem saldo suficiente ###")
    #Exedeu o Limite
    elif valor > limite: 
        print("### Operação falhou! O valor execede o limite ###")
    #Exedeu o Numero de Saques
    elif numero_saques > limite_saques: 
        print("### Operação falhou! Numero de saque maximo execedido ###")
    #Erro de Entrada
    else:
        print("### Operação falhou! O valor informado é invalido ###")    

    return saldo, extrato

#Função de EXTRATO: Recebe 'Positonal & Keyword Only'
def exibir_extrato(saldo, /, *, extrato):
    print("\n================EXTRATO==============")
    print(extrato if extrato != "" else "Não foram realizados movimentações")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=====================================")

#Função de Criação de Novo Usuario
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios) #Verifica existência do Usuario

    #Se o usuario já é cadastrado 
    if usuario:
        print("\n### Já existe usuário com esse CPF! ###")
        return
    
    #Se o usuario ainda não é cadastrado (continua o processo...)
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    #Adiciona o novo usuario a lista 'usuarios'
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("### Usuário criado com sucesso! ###")

#Função procurar por Usuario
def filtrar_usuario(cpf, usuarios):
    #Procura pelo registro do cpf dentro da lista 'usuarios'
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Função de Criação de Nova Conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios) #Verifica existência do Usuario

    #Se o usuario já é cadastrado cria conta
    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n### Usuário não encontrado, fluxo de criação de conta encerrado! ###")

#Função Lista as contas Criadas
def listar_contas(contas):
    #Laço pecorre a lista 'contas' e mostra Agencia,Numero da conta e Usuario
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#Função main
def main():
    # Variaveis
    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    #Laço para automatizar o Dialogo (Operações Bancarias)
    while True:
        opcao = menu()

        #Opção de Deposito
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato) #Chama a função 'depositar'=> Paramêtros:Posicional Only

        #Opção de Saque
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar( #Chama a função 'sacar'=> Paramêtros:Keyword Only
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        #Opção de Extrato
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato) #Chama a função 'exibir_extrato'=> Paramêtros:Posicional & Keyword

        #Opção de Criar Usuaria
        elif opcao == "4":
            criar_usuario(usuarios) #Chama a função 'criar_usuario'

        #Opção de Criar Conta
        elif opcao == "5":
            numero_conta = len(contas) + 1 #Conta a quantidade de Contas
            conta = criar_conta(AGENCIA, numero_conta, usuarios) #Chama a função 'criar_contas'

            if conta:
                contas.append(conta) #Adiciona a nova conta a lista 'contas'

        #Opção de Listar Contas
        elif opcao == "6":
            listar_contas(contas)

        #Opção de Saida (Fim do Laço)*
        elif opcao == "0":
            break

        #Erro de Entrada
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main() #Entrada automatica do Codigo Criado
#Fim
