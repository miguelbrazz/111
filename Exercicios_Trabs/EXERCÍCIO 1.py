"""
Exercício de revisão 01

Faça um algoritmo que, através da digitação pelo teclado, armazene
em uma lista vários nomes de cidades brasileiras.

Exemplo:
Digite uma nova cidade: CANOAS

Seu programa deverá utilizar o seguinte menu:


Menu
0- Finalizar o Programa
1- Cadastrar cidades
2- Listar as cidades cadastradas
3- Alterar o nome de alguma cidade digitada erradamente
4- Excluir uuma cidade da lista
Escolha:

Obs:
- Você não deve aceitar duas cidades com o mesmo nome.

"""

lista_de_cidade = []


def adicionar_cidade():
    """ Esta função tem o onjetivo de adicionar uma nova
        cidade na lista.
    """
    nome_cidade = input('...Nome da cidade: ')
    lista_de_cidade.append(nome_cidade)



#   lista_de_cidades.append(input('...Nome da cidade: '))



def listar_cidades():
    """ Esta função tem a finalidade de mostrar todas as
        cidades da lista_de_cidades.
    """
    print(lista_de_cidade)





def alterar_cidade():
    """ Esta função tem a finalidade de alterar o nome
        de alguma cidade.
    """
    nome_cidade = input('...Nome da cidade: ')
    if nome_cidade in lista_de_cidade:
        posicao_na_lista = lista_de_cidade.index(nome_cidade)
        lista_de_cidade[posicao_na_lista] = input('...Novo nome da cidade: ')





def excluir_cidade():
    """ Esta função tem a finalidade de retirar o nome de uma cidade
        da lista de cidades.
    """
    nome_cidade = input('...Nome da cidade: ')
    if nome_cidade in lista_de_cidade:
        lista_de_cidade.remove(nome_cidade)





# Programa - Início
while True:
    resposta = input\
        ("""

        Menu
            0- Finalizar o Programa
            1- Cadastrar cidades
            2- Listar as cidades cadastradas
            3- Alterar o nome de alguma cidade digitada erradamente
            4- Excluir uma cidade da lista
        Escolha: """
        )
    if resposta == '0':
        break
    if resposta == '1': adicionar_cidade()
    if resposta == '2': listar_cidades()
    if resposta == '3': alterar_cidade()
    if resposta == '4': excluir_cidade()

               











    
