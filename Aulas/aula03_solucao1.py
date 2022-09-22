"""
Exercício utilizando Listas

Faça um algoritmo que, através da digitação pelo teclado, armazene várias cidades e seus estados.

Exemplo da estrutura das listas:
lista_de_cidades	lista_de_estados
0 	PORTO ALEGRE	RIO GRANDE DO SUL
1	CANOAS		    RIO GRANDE DO SUL
2	GRAVATAI		RIO GRANDE DO SUL
3	FLORIANÓPOLIS	SANTA CATARINA
4	TUBARÃO		    SANTA CATARINA
5	SANTA MARIA		RIO GRANDE DO SUL



Exemplo da digitação dos dados:
Digite uma nova cidade: CANOAS
Digite o estado desta cidade: RIO GRANDE DO SUL

Seu programa deverá utilizar o seguinte menu:

Menu
0-	Finalizar o Programa
1-	Adicionar cidades e estados
2-	Listar as cidades e seus respectivos estados
3-	Alterar o nome de uma cidade
4-	Alterar o nome de um estado
5-	Listar todas as cidades de um determinado estado
6-	Retirar da lista uma cidade ou estado
Escolha:

Obs:
- Você não deve aceitar duas cidades com o mesmo nome, nem estado.
- A opção 2 deverá ser no seguinte formato:
	Relatório Geral:
	Cidade: CANOAS		Estado: RIO GRANDE DO SUL
	Cidade: PORTO ALEGRE	Estado: RIO GRANDE DO SUL
	Cidade: GRAVATAI		Estado: RIO GRANDE DO SUL
	Cidade: FLORIANÓPOLIS	Estado: SANTA CATARINA
	Cidade: TUBARÃO		Estado: SANTA CATARINA

- A Opção 5, deverá pedir ao usuário para escolher um estado e listar todas as cidades deste estado. Exemplo:
Escolha o estado: SANTA CATARINA
As cidades deste estado são:
- FLORINÓPLIS
- TUBARÃO

- Ao excluir um estado, não esqueça de excluir também todas as cidades relacionadas a este estado.

"""



""" Lista de cidades """
lista_de_cidades = list()
lista_de_cidades = ["PORTO ALEGRE", "CANOAS","SANTA MARIA", "FLORIANÓPOLIS"]
#========================================================

def adiciona_elemento_na_lista_de_cidades(nome_cidade):
    """ Realiza a insersão do elemento na lista"""
    lista_de_cidades.append(nome_cidade)

def remove_elemento_da_lista_de_cidades(nome_cidade):
    """ Retira um elemento da lista. """
    posicao = lista_de_cidades.index(nome_cidade)
    remove_elemento_da_lista_de_estados_pelo_indice(posicao)
    lista_de_cidades.remove(nome_cidade)

def remove_elemento_da_lista_de_cidades_de_um_estado(posicao):
    lista_de_cidades.pop(posicao)

def altera_elemento_da_lista_de_cidades(novo_nome_cidade, posicao):
    """ Modifica um elemento na posição correta da lista. """
    lista_de_cidades[posicao] = novo_nome_cidade

def elemento_esta_na_lista_de_cidades(cidade):
    """ Verifica se elemento está na lista e retorna True, caso esteja
        e False caso não esteja."""
    if cidade in lista_de_cidades: return True
    return False

def mostra_elementos_individualmente_da_lista_de_cidades():
    print("---Cidades inseridas na lista:")
    for nome_cidade in lista_de_cidades:
        print("   -",nome_cidade)

def get_cidade(posicao):
    return lista_de_cidades[posicao]

def get_tam_lista_cidades():
    return len(lista_de_cidades)








""" lista de estados """
lista_de_estados = list()
lista_de_estados = ["RIO GRANDE DO SUL", "RIO GRANDE DO SUL","RIO GRANDE DO SUL","SANTA CATARINA"]
#========================================================

def adiciona_elemento_na_lista_de_estados(nome_estado):
    """ Realiza a insersão do elemento na lista"""
    lista_de_estados.append(nome_estado)

def remove_elemento_da_lista_de_estados_pelo_indice(indice):
    lista_de_estados.pop(indice)

def remove_elemento_da_lista_de_estados(nome_estado):
    """ Retira um elemento da lista. """
    lista_de_indices = []
    for posicao, estado in enumerate(lista_de_estados):
        if nome_estado == estado:
            lista_de_indices.append(posicao)
    print(lista_de_indices)
    lista_de_indices.reverse()
    print(lista_de_indices)
    for posicao in lista_de_indices:
        remove_elemento_da_lista_de_cidades_de_um_estado(posicao)
        remove_elemento_da_lista_de_estados_pelo_indice(posicao)


def altera_elemento_da_lista_de_estados(nome_estado_velho, novo_nome_estado):
    """ Modifica um elemento na posição correta da lista. """
    for posicao,estado in enumerate(lista_de_estados):
        if estado == nome_estado_velho:
            lista_de_estados[posicao] = novo_nome_estado

def elemento_esta_na_lista_de_estados(estado):
    """ Verifica se elemento está na lista e retorna True, caso esteja
        e False caso não esteja."""
    if estado in lista_de_estados: return True
    return False

def mostra_elementos_individualmente_da_lista_de_estados():
    print("---Estados inseridos na lista:")
    for nome_estado in list(set(lista_de_estados)):
        print("   -",nome_estado)

def get_estado(posicao):
    return lista_de_estados[posicao]









""" Menu """
def menu_principal():
    return input(("\n"*8) + """ 
                    
            Menu
            0-	Finalizar o Programa
            1-	Adicionar cidades e estados
            2-	Listar as cidades e seus respectivos estados
            3-	Alterar o nome de uma cidade
            4-	Alterar o nome de um estado
            5-	Listar todas as cidades de um determinado estado
            6-	Retirar da lista uma cidade ou estado
            Escolha: """)


def menu_retirar_lista():
    return input(""" 
                    
            Menu
            1-	Retirar Cidade da lista
            2-	Retirar Estado da lista
            Escolha:""")





def adicionar_cidade():
    """ Esta função tem o objetivo de adicionar uma nova
        cidade na lista de cidades.
    """
    mostra_elementos_individualmente_da_lista_de_cidades()
    while True:
        nome_cidade = input("...Adicione uma Nova Cidade à lista:\n...Nome da cidade: ").upper()
        if not elemento_esta_na_lista_de_cidades(nome_cidade):
            adiciona_elemento_na_lista_de_cidades(nome_cidade)
            break
        else: input("-----Cidade já consta na lista. [Enter]")


def adicionar_estado():
    """ Esta função tem o objetivo de adicionar um novo
        estado na lista de estados.
        - lista os estados existentes (caso lista não vazia)
        - adiciona um estado novo ou existente.
    """
    mostra_elementos_individualmente_da_lista_de_estados()
    while True:
        nome_estado = input("...Escolha um Estado ou Digite um Novo.\n...Nome do estado: ").upper()
        if not elemento_esta_na_lista_de_estados(nome_estado):
            resposta = input("..... Estado não consta na lista. Inserir? s/n: ").lower()
            if resposta == "n":
                continue
        adiciona_elemento_na_lista_de_estados(nome_estado)
        break


def listar_cidades():
    """ Esta função tem a finalidade de mostrar todas as
        cidades da lista_de_cidades e seu estado.
    """
    print("\n"*5)
    print("=-=-=-=- Cidades existentes na lista:")
    for x in range(get_tam_lista_cidades()):
        print(f"Cidade {get_cidade(x).ljust(30,'.')}     Estado: {get_estado(x)}")
    input("[Enter]")


def mostra_cidades_do_estado(estado_escolhido):
    print("--- Cidades do estado",estado_escolhido)
    for posicao,cidade in enumerate(lista_de_cidades):
        if get_estado(posicao) == estado_escolhido:
            print("   -Cidade:",cidade)


def mostrar_cidades_por_estado():
    print("--- Estados Existentes:")
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
    while True:
        nome_cidade = input("...Nome da cidade a ser alterado: ").upper()
        if elemento_esta_na_lista_de_cidades(nome_cidade):
            novo_nome_cidade = input("...Novo nome da cidade: ").upper()
            if not elemento_esta_na_lista_de_cidades(novo_nome_cidade):
                posicao_na_lista = lista_de_cidades.index(nome_cidade)
                altera_elemento_da_lista_de_cidades(novo_nome_cidade,posicao_na_lista)
                break
            else: input("-----Cidade já consta na lista. [Enter]")
        else: input("-----Cidade não consta na lista. [Enter]")


def alterar_estado():
    """ Esta função tem a finalidade de alterar o nome de
        algum estado.
    """
    while True:
        nome_estado_atual = input("...Nome do estado para alterar: ").upper()
        if elemento_esta_na_lista_de_estados(nome_estado_atual):
            novo_nome_estado = input("...Novo nome do estado: ").upper()
            altera_elemento_da_lista_de_estados(nome_estado_atual,novo_nome_estado)
            return
        else: input("-----Estado digitado não consta na lista. [Enter]")
        alterar_estado()


def excluir_cidade():
    """ Esta função tem a finalidade de retirar o nome de uma cidade da lista
        de cidades.
    """
    mostra_elementos_individualmente_da_lista_de_cidades()
    while True:
        nome_cidade = input("...Nome da cidade para retirar da lista: ").upper()
        if elemento_esta_na_lista_de_cidades(nome_cidade):
            remove_elemento_da_lista_de_cidades(nome_cidade)
            break
        else: input("-----Cidade não consta na lista. [Enter]")


def excluir_estado():
    """ Esta função tem a finalidade de retirar o nome de um estado da lista
        de estados, retirando também as cidades vinculadas a este estado.
    """
    mostra_elementos_individualmente_da_lista_de_estados()
    while True:
        nome_estado = input("...Nome do estado para retirar da lista: ").upper()
        if elemento_esta_na_lista_de_estados(nome_estado):
            remove_elemento_da_lista_de_estados(nome_estado)
            break
        else: input("-----Estado não consta na lista. [Enter]")


def retirar_cidade_ou_estado():
    resposta = menu_retirar_lista()
    if resposta == '1':
        excluir_cidade()
    if resposta == '2':
        excluir_estado()


def adicionar_cidade_estado():
        adicionar_cidade()
        adicionar_estado()





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



