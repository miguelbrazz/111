"""
Crie uma classe Pet, com os seguintes atributos:
    -Raça -> string
    -Porte-> string
    -Nome -> string

Crie uma classe Pessoa com os seguintes atributos:
    -Nome -> string
    -Telefone -> string
    -Endereço -> string
    -Pets -> lista de pets


Seu Programa deverá ler um arquivo 'arqPets.txt' com 2 informações:
    raça e porte, nesta ordem, e criar uma lista de Pets (l_Pets)
    instanciados do arquivo lido e armazenados na lista.
    - Na instância coloque o nome do animal como None. Pois o nome
        será dado pelo dono no hora da adoção. (quando escolher o animal)

Seu programa também deverá ler outro arquivo 'arqPessoas.txt' com
    nome, telefone e endereço, nesta ordem e criar um dicionário
    para armazenar essas informações. A lista de Pets deve ser criada
    sem conteúdo, pois será acrescida no dicionário conforme as escolhas dos
    animais.
    O dicionário (d_Pessoas) deverá ser populado com a chave sendo um
    número sequencial iniciando em 1 e o valor deverá ser um objeto
    da classe Pessoa.

Crie uma função onde você deverá selecionar do dicionário uma pessoa,
    listar os animais (l_Pets) para serem doados,
    e escolher um ou mais Pets para serem adotados pelas pessoas.
    (adicionando no atributo pets)

Desenvolva as funções ou métodos que achar necessários para executar
essa tarefa.

"""

class Pet:
    def __init__(self,raca,porte):
        self.raca = raca
        self.porte = porte
        self.nome = None

    def __str__(self):
        return f"{self.raca} {self.porte}"# {str(self.nome)}"

    def set_nome(self,novo_nome):
        self.nome = novo_nome

    def get_nome_pet(self):
            return str(self.nome)

class Pessoa:
    def __init__(self,nome,telefone,endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.pets = []

    def possui_pet(self):
        if len(self.pets) > 0:
            return True
        return False

    def get_nome_pets(self):
        st_pets = " "
        for pet in self.pets:
            st_pets += str(pet.get_nome_pet())+"; "
        return st_pets

    def adicionar_pet(self,pet):
        self.pets.append(pet)

    def mostrar_pessoas_possuem_pet(self):
            return f"{self.nome} >> {self.get_nome_pets()}"


    def mostra_nome_pessoas(self):
        return f"{self.nome}"


    def __str__(self):
        return f"{self.nome}  {self.telefone}  {self.endereco} {self.get_nome_pets()}"

l_pets = []
def mostra_pets():
    print("\n=-=-=-=- Animais para adoção:")
    for i,pet in enumerate(l_pets):
        print(f"{str(i)}-{pet}")

def ler_arquivo_pets():
    """ Lê arquivo arq_pets, instancia a classe Pet e popula a l_pets"""
#    arq = open("Pets/nda.txt","w")
    arq = open("Pets/arqPets.txt", "r")
    for a in arq:
        raca = a.split(",")[0]
        porte= a.split(",")[1].strip("\n")
        pet = Pet(raca,porte)
        l_pets.append(pet)
    arq.close()



d_pessoas = {}
def mostra_pessoas():
    print("-----Pessoas dispostas a adotar: ")
    for i,p in d_pessoas.items():
        print(i,p.mostra_nome_pessoas())

def mostrar_pessoas_que_adotaram():
    print("-----Pessoas que adotaram: ")
    for i,p in d_pessoas.items():
        if p.possui_pet():
            print(i,p.mostrar_pessoas_possuem_pet())


def ler_arquivo_pessoas():
    """ Lê arquivo arqPessoas, instancia a classe Pessoa e popula o d_pessoas """
    arq = open("Pets/arqPessoas.txt", "r")
    for i,a in enumerate(arq):
        nome = a.split(";")[0]
        telefone = a.split(";")[1]
        endereco = a.split(";")[2].replace("\n","") # strip("\n")
        d_pessoas[i+1] = Pessoa(nome,telefone,endereco)

def adotar_pet():
    """ Função que realiza a doação do pet"""
    while True:
        print("\n"*3)
        mostra_pessoas()
        pessoa_selecionada = input("Escolha uma das pessoas da lista (ind.): ")
        if d_pessoas[int(pessoa_selecionada)]:
            mostra_pets()
            pet_escolhido = input("Escolha um dos pets da lista: ")
            nome_pet = input("...Dê um nome para o seu pet: ")
            l_pets[int(pet_escolhido)].set_nome(nome_pet)
            d_pessoas[int(pessoa_selecionada)].adicionar_pet(l_pets[int(pet_escolhido)])
        mostrar_pessoas_que_adotaram()


ler_arquivo_pets()

ler_arquivo_pessoas()

adotar_pet()


