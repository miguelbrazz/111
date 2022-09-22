
'''
Faça um programa que simule o uso de um abajur.
As caracteristicas do abajur são: Botão, Quantidade de Leds, Cor, Intensidade e Carga da Bateria
Em nosso abajur existe apenas um botão. Este possui 4 estágios. Cada toque no botão passa para um
dos estágios: 0,1,2,3. Estando no estágio 3 o próximo passa a zero novamente:
        primeiro - 0, indica abajur apagado
        segundo  - 1, indica ligado, mas intensidade FRACA
        terceiro - 2, indica ligado, mas intensidade MEDIA
        quarto   - 3, indica ligado, com intensidade FORTE
A cada toque no botão você deverá atualizar a intensidade e a carga da bateria. A carga deverá
ser atualizada conforme os seguintes critérios:
    quando o botão estiver no estágio 1 - atualizar o consumo em -2% (menos 2 porcento)
    quando o botão estiver no estágio 2 - atualize  o consumo em -4% (menos 4 porcento)
    quando o botão estiver no estágio 3 - atualize  o consumo em -6% (menos 6 porcento)

Quando a carga estiver em 0% exiba a mensagem: "Bateria descarregada" e não ligue o abajur.

Passo a passo:
==============

Crie uma classe chamada Abajur.
Crie o construtor com os seguintes atributos:
    - botão: em zero.
    - intensidade em "APAGADA"
    - quantidade de leds: 15
    - cor: deve ser passada por parâmetro.
    - quantidade da carga: em zero

Crie um método para carregar a bateria
Crie um método simular o aperto do botão do abajur.
Crie um método para setar o atributo intensidade. Conforme o valor do Botão
    - botão 0 - intensidade "APAGADA"
    - botão 1 - intensidade "FRACA"
    - botão 2 - intensidade "MEDIA"
    - botão 3 - intensidade "FORTE"

Crie um método para atualizar a garga:
    - Quando o botão estiver em 1, atualize a carga em menos 2%
    - Quando o botão estiver em 2, atualize a carga em menos 4%
    - Quando o botão estiver em 3, atualize a carga em menos 6%

Crie um método que retorna o status dos atributos para impressão.

'''

class Abajur:
    def __init__(self, cor):
        self.botao       = 0
        self.intensidade = 'APAGADA'
        self.leds        = 15
        self.cor         = cor
        self.carga       = 0

    def carregar(self):
        self.carga = 100

    def set_botao(self):
        if self.carga <= 0:
            input("... Bateria descarregada.")
            return

        self.botao += 1
        if self.botao == 4:
            self.botao = 0
        self.set_intensidade()
        self.set_carga()

    def set_intensidade(self):
        if self.botao == 0:
            self.intensidade = "APAGADA"
        if self.botao == 1:
            self.intensidade = "FRACA"
        if self.botao == 2:
            self.intensidade = "MEDIA"
        if self.botao == 3:
            self.intensidade = "FORTE"

    def set_carga(self):
        if self.botao == 1:
            self.carga  =  self.carga - (2 * self.carga / 100)
        if self.botao == 2:
            self.carga  =  self.carga - (4 * self.carga / 100)
        if self.botao == 3:
            self.carga  =  self.carga - (6 * self.carga / 100)

    def __str__(self):
        return ">>> Cor: "+self.cor + "  Botão: " + str(self.botao) + "  Intes.: " + self.intensidade + \
            "  Carga: " + str(self.carga)

    # def get_dados(self):
    #     return ">>> Cor: "+self.cor + "  Botão: " + str(self.botao) + "  Intes.: " + self.intensidade + \
    #         "  Carga: " + str(self.carga)


################ Principal

lista_abajur = []
abajur1 = Abajur(input("... Digite a cor: "))
abajur2 = Abajur(input("... Digite a cor: "))

lista_abajur.append(abajur1)

while True:
    print(abajur1)   #print(abajur.get_dados())
    print(abajur2)

    e = input('''
    
    Menu:
    1- Apertar o Botão.
    2- Carregar a bateria.
    3- escolha o abajur.
    escolha: ''')

    if e == '1':
        abajur.set_botao()
    if e == '2':
        abajur.carregar()
    if e == "3":
        a = input("\nEscolha: 1- Abajur1  2- Abajur2 : ")
        if a == "1":
            abajur = abajur1
        if a == "2":
            abajur = abajur2
