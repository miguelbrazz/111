
"""
O que Preciso saber para prosseguir?

1 - Variáveis -> int, float, string, bool, listas
2 - Operadores-> Aritméticos, Relacionais e Boleanos
3 - funções   -> print(), input(), int()
4 - comandos  -> if elif else,  for,  while
"""

# --------------------------------------------------------

''' ------ Exemplo 1 -------'''
def minhaFuncao():
    print("Estamos iniciando o semestre (Fudeu).")
    print("Boa Sorte a Todos Nós.(Vamos precisar pqp) ")

# programa principal
minhaFuncao()


''' ------ Exemplo 2 -------'''
def minhaFuncao():
    return "Meu nome é Mig. "

# programa principal
print (minhaFuncao())



''' ------ Exemplo 3 -------'''
def minhaFuncao(argumento):
    print (argumento)

# programa principal
texto = input("Digite algo: ")
minhaFuncao(texto)


''' ------ Exemplo 4 -------'''
def minhaFuncao(idade):
    if idade < 14 :
        resultado =  "Criança :D"
    elif idade < 18 :
        resultado = "Adolecente :D"
    elif idade < 65:
        resultado = "Adulto D:"
    else :
        resultado = "Idoso D:"

    return resultado

# programa principal
seuNome  = input("Digite seu nome: ")
suaIdade = int(input("Digite sua idade: ") )
print ( seuNome,"você é" , minhaFuncao(suaIdade) )
