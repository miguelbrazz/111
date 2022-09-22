
menu = ''' \n\n\nMenu
    0-  Finalizar
    1-	Cadastrar salas na lista
    2-	Listar salas cadastradas
    3-	Alterar a numeração de alguma sala
    4-	Excluir uma sala da lista
    5-  Relatório de salas por andar
Escolha: '''

listaDeSalas      = []
num = []
qntdDeAlunos = []
qntdDeComputadores = []

#########################################################
# Cadastro 1
def cadastrarSala():
    salaDigitada = input("Digite a sala: ")
    alunos = input("Quantidade de alunos: ")
    computadores = input("Quantidade de computadores: ")
    listaDeSalas.append(salaDigitada)
    num.append(salaDigitada)
    qntdDeAlunos.append(alunos)
    qntdDeComputadores.append(computadores)
#########################################################




#########################################################
# Relatório de Salas Cadastradas 2
def relatorioSalas():
    for sala in listaDeSalas:
        print(sala)
#########################################################




#########################################################
# Alterar a numeração da sala 3
def alterarSala():
    
    print("... Salas Cadastradas")
    for sala in listaDeSalas:
        print(sala)

    print("... Escolha uma das salas:")
    salaEscolhida = input()

    if salaEscolhida in listaDeSalas:
        novaSala = input("... Digite a nova numeração para a sala: ")
        if novaSala in listaDeSalas:
            input("... Esta numeração já consta no cadastro. [Enter] ...")
        else:
            indiceSala = listaDeSalas.index(salaEscolhida)
            listaDeSalas[indiceSala] = novaSala
    else:
        input("...Sala não cadastrada. [Enter]")
        
#########################################################




#########################################################
# Excluir sala - 4
def excluirSala():
    print("... Salas Cadastradas")
    for sala in listaDeSalas:
        print(sala)
    
    salaDigitada = input('Digite o número da sala a ser excluida: ')
    if salaDigitada in listaDeSalas:
        #Está na lista
        listaDeSalas.remove(salaDigitada)
        input("... Sala Removida da Lista. [Enter] ....")
    else:
        #Não está na lista
        input("... Sala não consta na lista. [Enter] ...")



        
#########################################################
# Registrar Salas por andar - 5
def relatorioAndar():
    print("Salas por Andar")
    for salaDigitada in listaDeSalas:
        print("Sala:",salaDigitada)
    for num in salaDigitada[0]:
        print("Andar:",num[0])
    for alunos in qntdDeAlunos:
        print("Quantidade de alunos:",alunos)
    for computadores in qntdDeComputadores:
        print("Quantidade de computadores:",computadores)
        
#-=-=-=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Programa Pricipal
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        print("\nCadastrar Salas na lista")
        cadastrarSala()
    elif escolha == '2':
        print("\nListar as Salas Cadastradas")
        relatorioSalas()
    elif escolha == '3':
        print("\nAlterar a numeração de alguma Sala")
        alterarSala()
    elif escolha == '4':
        print("\nExcluir uma Sala da Lista")
        excluirSala()
    elif escolha == '5':
        print("\nRelatório de salas por andar")
        relatorioAndar()
    else:
        input("\n\n=== Finalizar o Programa ===")



