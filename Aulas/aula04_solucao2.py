from Ano2021_1.aula04_solucao2_menus import *
from Ano2021_1.aula04_solucao2_listas import *



""" Funções do programa principal """

def ler_teclado(mensagem):
    return input(mensagem).upper()

def adicionar_cidade():
    """ Esta função tem o objetivo de adicionar uma nova
        cidade na lista de cidades. O nome das cidades não devem repetir-se na lista.
    """
    print("\n"*5)
    if not lista_cidades_vazia():
        mostra_elementos_individualmente_da_lista_de_cidades()
    nova_cidade = ler_teclado("...Adicione uma Nova Cidade à lista:\n...[Enter]Retorna ao menu.\n...Nome da cidade: ")
    if not nova_cidade:
        return
    if not elemento_esta_na_lista_de_cidades(nova_cidade):
            adiciona_elemento_na_lista_de_cidades(nova_cidade)
            adicionar_estado()
    else: input("-----Cidade já consta na lista. [Enter]")
    adicionar_cidade()


def adicionar_estado():
    """ Esta função tem o objetivo de adicionar um novo
        estado na lista de estados.
        - lista os estados existentes (caso lista não vazia)
        - adiciona um estado novo ou existente.
    """

    estado = seleciona_estado().upper()
    adiciona_elemento_na_lista_de_estados(estado)


def listar_cidades():
    """ Esta função tem a finalidade de mostrar todas as
        cidades da lista_de_cidades e seu estado.
    """
    print("\n"*5)
    if lista_cidades_vazia():
        input("\n\n-----Não há cidades inseridas na lista. [Enter]")
        return

    print("\n\n=-=-=-=- Cidades existentes na lista:")
    for x in range(get_tam_lista_cidades()):
        print(f"Cidade {get_cidade(x).ljust(30,'.')}     Estado: {get_estado(x)}")

    input("[Enter]")


def mostra_cidades_do_estado(estado_escolhido):
    print("--- Cidades do estado",estado_escolhido)
    for posicao,cidade in enumerate(lista_de_cidades):
        if get_estado(posicao) == estado_escolhido:
            print("   -Cidade:",cidade)


def mostrar_cidades_por_estado(): #
    print("\n\n--- Estados Existentes:")
    mostra_elementos_individualmente_da_lista_de_estados()
    estado_escolhido = input("Escolha um Estado da Lista: ").upper()
    if elemento_esta_na_lista_de_estados(estado_escolhido):
        mostra_cidades_do_estado(estado_escolhido)
    else: print("---Elemento não encontrado na lista. ")
    input("[Enter]")


def alterar_cidade():
    """ Esta função tem a finalidade de alterar o nome de
        alguma cidade.
    """
    nome_cidade = seleciona_cidade()
    if not nome_cidade:
        return

    novo_nome_cidade = input("...Novo nome da cidade: ").upper()
    if not elemento_esta_na_lista_de_cidades(novo_nome_cidade):
                posicao_na_lista = lista_de_cidades.index(nome_cidade)
                altera_elemento_da_lista_de_cidades(novo_nome_cidade,posicao_na_lista)
    else:
        input("-----Cidade já consta na lista. [Enter]")
        alterar_cidade()


""" """


def alterar_estado(): # TEMA: Refazer utizando a escolha por menu.

    """ Esta função tem a finalidade de alterar o nome de
        algum estado.
    """
    pass
    # while True:
    #     nome_estado_atual = input("...Nome do estado para alterar: ").upper()
    #     if elemento_esta_na_lista_de_estados(nome_estado_atual):
    #         novo_nome_estado = input("...Novo nome do estado: ").upper()
    #         altera_elemento_da_lista_de_estados(nome_estado_atual,novo_nome_estado)
    #         break
    #     else: input("-----Estado digitado não consta na lista. [Enter]")


def excluir_cidade():
    """ Esta função tem a finalidade de retirar o nome de uma cidade da lista
        de cidades.
    """
    nome_cidade = seleciona_cidade()
    if not nome_cidade:
        return

    remove_elemento_da_lista_de_cidades(nome_cidade)


def excluir_estado(): # TAREFA para os alunos - Retirar pela escolha de um menu
    """ Esta função tem a finalidade de retirar o nome de um estado da lista
        de estados, retirando também as cidades vinculadas a este estado.
    """
    mostra_elementos_individualmente_da_lista_de_estados()
    # while True:
    #     nome_estado = input("...Nome do estado para retirar da lista: ").upper()
    #     if elemento_esta_na_lista_de_estados(nome_estado):
    #         remove_elemento_da_lista_de_estados(nome_estado)
    #         break
    #     else: input("-----Estado não consta na lista. [Enter]")


def retirar_cidade_ou_estado():
    resposta = menu_retirar_lista()
    if resposta == '1':
        excluir_cidade()
    if resposta == '2':
        excluir_estado()


def adicionar_cidade_estado():
    adicionar_cidade()



# Programa - Início
while True:
    resposta = menu_principal()
    if resposta == '0':break
    elif resposta == '1': adicionar_cidade_estado()
    elif resposta == '2': listar_cidades()
    elif resposta == '3': alterar_cidade()
    elif resposta == '4': alterar_estado()
    elif resposta == '5': mostrar_cidades_por_estado()
    elif resposta == '6': retirar_cidade_ou_estado()

