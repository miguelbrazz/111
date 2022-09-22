
""" Lista de cidades """
lista_de_cidades = list()
#lista_de_cidades = ["PORTO ALEGRE", "CANOAS","SANTA MARIA", "FLORIANÓPOLIS"]
#========================================================
def escolher_cidade():
    mostra_elementos_individualmente_da_lista_de_cidades()
    #escolha =

def lista_cidades_vazia():
    if len(lista_de_cidades) == 0:
        return True
    return False

def adiciona_elemento_na_lista_de_cidades(nome_cidade):
    """ Realiza a insersão do elemento na lista"""
    lista_de_cidades.append(nome_cidade)

def remove_elemento_da_lista_de_cidades(nome_cidade):
    """ Retira um elemento da lista cidade e lista estado. """
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

def mostra_menu_cidades():
    print("\n\n----- Cidades Inseridas:")
    print(f"   Indice  Cidade")
    for indice,cidade in enumerate(lista_de_cidades):
        print(f"   {indice+1}       {cidade}")

def seleciona_cidade():
    if lista_cidades_vazia():
        input("\n\n-----Não há cidades inseridas na lista. [Enter]")
        return None

    mostra_menu_cidades()

    cidade = input("\n...Escolha uma cidade pelo indice: ")

    try:
        return get_cidade(int(cidade)-1)
    except:
        input("----- Escolha inválida. [Enter]")
    return seleciona_cidade()

def get_cidade(posicao):
    return lista_de_cidades[posicao]

def get_tam_lista_cidades():
    return len(lista_de_cidades)
""" Lista de cidades fim """




""" lista de estados """
lista_de_estados = list()
#lista_de_estados = ["RIO GRANDE DO SUL", "RIO GRANDE DO SUL","RIO GRANDE DO SUL","SANTA CATARINA"]
#========================================================
def lista_estados_vazia():
    if len(lista_de_estados) == 0:
        return True
    return False

def estado_existe_na_lista(estado):
    if estado in lista_de_estados:
        return True
    return False

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

def mostra_menu_estados():
    estados_nao_repetidos = sorted(set(lista_de_estados))
    print("\n\n----- Estados Inseridos:")
    print(f"   Indice  Estado")
    #for indice,estado in enumerate(lista_de_estados):
    for indice,estado in enumerate(estados_nao_repetidos):
        print(f"   {indice+1}       {estado}")

def get_estado(posicao):
    return lista_de_estados[posicao]

def seleciona_estado(): # tarefa para os alunos: COMENTAR esta função
    mensagem = ":"
    if not lista_estados_vazia():
        mostra_menu_estados()
        mensagem = " ou \n...Escolha pelo indice: "
    estado = input("\n\n...Digite um novo estado para inserir"+mensagem)
    if not estado.isnumeric():
        if not estado_existe_na_lista(estado):
            while True:
                duvida = input("...Inserir na lista como novo estado? s/n: ").lower()
                if duvida in ["s","n"]:
                    if duvida == 'n':
                        continue
                    break
                else:
                    input("-----Favor escolher somente s/n.")
                    return seleciona_estado()
        return estado
    try:
        return get_estado(int(estado)-1)
    except:
        input("----- Escolha inválida. [Enter]")
    return seleciona_estado()

""" lista de estados  fim """

