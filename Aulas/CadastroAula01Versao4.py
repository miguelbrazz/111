# Solução do Primeiro exercício - versão 4
# Autor: Ivonei Marques

menu = '''
+--------------------------------------------+
|Menu                                        |
+--------------------------------------------+
|    0-  Finalizar                           |
|    1-	Cadastrar sala na lista              |
|    2-	Listar salas cadastradas             |
|    3-	Alterar a numeração de alguma sala   |
|    4-	Excluir uma sala da lista            |
|    5-	Relatório de sala por andar          |
+--------------------------------------------+
Escolha: '''

menu_alteracao = '''
  +---------------------------------+
  |         Menu Alteração          |
  |  1- Sala                        |
  |  2-	Andar                       |
  |  3-	Capacidade da Sala          |
  |  4-	Quantidade de Computadores  |
  +---------------------------------+
    Escolha: '''


#==============================================
# Declaração das listas utilizadas no programa
listaDeSalas        = []
listaDeAndares      = []
listaDeCapacidades  = []
listaDeQtdeComps    = []

listaDeSalas        = ['201','301','401','202']
listaDeAndares      = ['2','3','4','2']
listaDeCapacidades  = [22,33,40,23]
listaDeQtdeComps    = [11,22,33,11]





def cabecalho():
    lista_cabecalho = [
        " ",
        "\nCadastro de Sala",
        "\nListar das Salas Cadastradas",
        "\nAlterar Salas ",
        "\nExcluir Salas",
        "\nRelatório de Salas por andar"
        ]
    print( lista_cabecalho[int(escolha)] )




def sala_validada():
    while True:
        sala = input("Digite a sala: ")
        if sala in listaDeSalas:
                input("\n=== Esta Sala já consta no cadastro. [Enter] ===")
        else:
            return sala

def andar_valido():
    return input("Digite o andar: ")

def validar_capacidade_da_sala():
    qtde_maxima = 40
    qtde_minima = 0
    while True:
        try:
            qtde = int(input("Digite a Capacidade da Sala: "))
            if qtde >= qtde_minima  and  qtde <= qtde_maxima:
                return qtde
            input("\n=== A capacidade deve estar entre 0 e 40. [Enter] ===")
        except:
            input("\n=== A capacidade deve ser um numeral. [Enter] ===")

def validar_qtde_computadores():
    qtde_minima = 0
    while True:
        try:
            qtde = int(input("Digite a quantidade de computadores na sala: "))
            if qtde >= qtde_minima:
                return qtde
            input("\n=== A quantidade deve ser maior ou igual a 0. [Enter] ===")
        except:
            input("\n=== A quantidade deve ser um numeral. [Enter] ===")




#########################################################
# Cadastro 1
def cadastrar_dados_sala():
    cabecalho()

    listaDeSalas.append(sala_validada())
    listaDeAndares.append(andar_valido())
    listaDeCapacidades.append(validar_capacidade_da_sala())
    listaDeQtdeComps.append(validar_qtde_computadores())

#########################################################






#########################################################
# Relatório de Salas Cadastradas 2
def relatorio_salas():
    cabecalho()    

    print("    sala - andar - capacidade pessoas - qtde computadores")
    print("    _____________________________________________________")
    for ind,sala in enumerate(listaDeSalas):
        print("    {0}{1}{2}{3}"
               .format(
                    str(sala).ljust(7), 
                    str(listaDeAndares[ind]).ljust(8),
                    str(listaDeCapacidades[ind]).center(21),
                    str(listaDeQtdeComps[ind]).center(18)
                    )
            )
    input(' [Enter] Continua...')

#########################################################







def escolhe_sala():
    relatorio_salas()

    sala = input("Escolha uma sala para Alterar: ")
    if sala in listaDeSalas:
        return listaDeSalas.index(sala)
    input('...Erro. Sala não consta no adastro. [Enter]')
    return escolhe_sala()
    


def altera_conforme(ind,opcao):
    if opcao == '1':
        listaDeSalas[ind]   = sala_validada()
    elif opcao == '2':
        listaDeAndares[ind] = andar_valido()
    elif opcao == '3':
        listaDeCapacidades[ind] = validar_capacidade_da_sala()
    else:
        listaDeQtdeComps[ind]   = validar_qtde_computadores()


def escolhe_que_alterar():
    escolha = input(menu_alteracao)
    if escolha in ('1','2','3','4'):
        return escolha
    input('...Opção não existe no menu. [Enter]')
    return escolhe_que_alterar()







#########################################################
# Alterar a numeração da sala 3
def alterar_dados_sala():
    cabecalho()

    altera_conforme(escolhe_sala(), escolhe_que_alterar())

#########################################################





#########################################################
# Excluir sala - 4
def excluir_sala():
    cabecalho()

    relatorio_salas()
    
    salaDigitada = input('Digite o número da sala a ser excluida: ')
    if salaDigitada in listaDeSalas:
        #Está na lista
        ind = listaDeSalas.index(salaDigitada)
        listaDeSalas      .remove(salaDigitada)
        listaDeAndares    .pop( ind )
        listaDeCapacidades.pop( ind )
        listaDeQtdeComps  .pop( ind )
        input("... Sala Removida da Lista. [Enter] ....")
    else:
        #Não está na lista
        input("... Sala não consta na lista. [Enter] ...")
#########################################################

def imprime_so_andares(lista_andares_cadastrados):
    print('Andares Cadastrados')
    print('-------------------')
    lista_andares_cadastrados.sort()
    for andar in lista_andares_cadastrados:
        print(' '*5,andar)



def andares_cadastrados(): 
    lista_andares_cadastrados = [] # cria lista somente com os andares cadastrados, sem repetição
    def identifica_os_andares():
        for andar in listaDeAndares:
            if andar not in lista_andares_cadastrados:
                lista_andares_cadastrados.append(andar)

    identifica_os_andares()
    imprime_so_andares(lista_andares_cadastrados)

def escolha_andar():
    andares_cadastrados()
    return input('Escolha o andar: ')

def salas_do_andar(andar):
    print(' '*8,'Salas do',andar,':')
    print(' '*8,'------------')
    for ind,sala in enumerate(listaDeSalas):
        if listaDeAndares[ind] == andar:
            print(' '*8,sala)

#########################################################
# Opção 5
def relatorio_por_andar():
    cabecalho()
    salas_do_andar(escolha_andar())
    input(' [Enter] Continua...')

#########################################################




#########################################################
#########################################################
# Programa Pricipal
#########################################################
escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        cadastrar_dados_sala()
    elif escolha == '2':
        relatorio_salas()
    elif escolha == '3':
        alterar_dados_sala()
    elif escolha == '4':
        excluir_sala()
    elif escolha == '5':
        relatorio_por_andar()
    else:
        input("\n\n=== Opção Inválida! [Enter] ===")



