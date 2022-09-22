class Pet:
    def __init__(self, raca, porte):
        self.raca = raca
        self.porte = porte
        self.nome = None

    def set_nome(self,nome):
        self.nome = nome

    def __str__(self):
        return f" {self.raca}  {self.porte} - {str(self.nome)}"


class Pessoa:
    def __init__(self,nome,telefone,endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.pets = []

    def set_pets(self,pet):
        self.pets.append(pet)

    def get_nome(self):
        return self.nome

    def pets_adotados(self):
        str = ""
        for pet in self.pets:
#            print(pet)
            str += pet.nome +"\n"
        return str

    def __str__(self):
        return f" {self.nome}  {self.pets_adotados()}"

# Populamos a lista
l_pets = []
arquivo = open("arqPets.txt","r")
for a in arquivo:
    raca = a.split(",")[0]
    porte= a.split(",")[1].replace("\n","")
    pet = Pet(raca,porte)
    l_pets.append(pet)
arquivo.close()


# Populamos o dicionário
d_pessoas = {}

with open('arqPessoas.txt', 'r') as arq_people:
    for i, a in enumerate(arq_people):
        nome = a.split(';')[0]
        telefone = a.split(';')[1]
        endereco = a.split(';')[2].replace("\n","")
        d_pessoas[i] = Pessoa(nome, telefone, endereco)
arq_people.close()

while True:
    # Escolhi uma pessoa
    for chave,p in d_pessoas.items():
        print(chave,p.get_nome())
    escolha = int(input("Escolha : "))

    #escolhi um pet
    for ind,pet in enumerate(l_pets):
        print(ind,pet)
    escolha_pet = int(input("Escolha Pet: "))

    # ler nome
    nome_pet = input("Nome Pet: ")

    # demos o nome ao pet
    l_pets[escolha_pet].set_nome(nome_pet)

    d_pessoas[escolha].set_pets(l_pets[escolha_pet])




    for p in d_pessoas.values():
        print(p)
