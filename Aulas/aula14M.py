"""Crie uma classe Onibus com os seguintes atributos
  numero_onibus:
  nome_motorista:
  poltronas:
obs. Todos atributos devem ser privados.
A quantidade de poltronas deverá ser uma lista fixa em 40
Crie uma lista com 4 Onibus diferentes."""

class Onibus:
  def __init__(self,numero_onibus=None,nome_motorista=None):
    self.set_numero(numero_onibus) #self.__numero = numero_onibus
    self.__nome_motorista = nome_motorista
    self.__poltronas = [ poltrona for poltrona in range(41)]

  def set_numero(self,numero):
      self.__numero = numero

  def get_numero(self):
      return self.__numero

  def reserva_poltrona(self,poltrona):
      self.__poltronas[poltrona] = " X"


  def __str__(self):
      return f"Onibus N. {self.__numero} Motorista: {self.__nome_motorista} \npoltronas: {self.__poltronas}"

"""Crie uma classe chamada Linha com os seguintes atributos privados.
  onibus:
  origem:
  destino:
  box_saida:
  hora_saida:
obs. o atibuto onibus deve ser escolhido da lista de onibus.
Crie uma lista com 4 linhas."""

class Linha:
  def __init__(self, onibus, origem, destino, box_saida, hora_saida):
    self.__origem = origem
    self.__destino = destino
    self.__box_saida = box_saida
    self.__hora_saida = hora_saida
    self.__onibus = onibus

  def get_onibus(self,poltrona):
      self.__onibus.reserva_poltrona(poltrona)

  def __str__(self):
      return f"Onibus: {self.__onibus} Destino: {self.__destino} Box: {self.__box_saida}"


"""Crie uma classe Passagem com os seguintes atributos:
  nome_passageiro:
  linha:
  poltrona:
obs. Todos atributos devem ser privados.
O passageiro deve informar o nome e a poltrona.
A linha deve ser escolhida da lista de linhas."""


class Passagem:
  def __init__(self, nome_passageiro, linha, poltrona):
    self.__nome_passageiro = nome_passageiro
    self.__linha  = linha
    self.__poltrona = poltrona
    self.reservar_poltrona(poltrona)

  def reservar_poltrona(self,poltrona):
      self.__linha.get_onibus(poltrona)

  def teste(self, nda):
      self.__linha = nda

  def __str__(self):
      return f"Passageiro:{self.__nome_passageiro} linha :{self.__linha}"



onibus1 = Onibus(111,"Pedro")
onibus2 = Onibus(112,"Pedro")
onibus3 = Onibus(113,"Pedro")


linhaA =  Linha(onibus1,"POA","Canoas",3,"09:00")
linhaB =  Linha(onibus3,"POA","Floripa",8,"19:00")



passagem = Passagem("Ivonei", linhaA,11)
passagem2= Passagem("MMMM",linhaB,22)

print(passagem)
