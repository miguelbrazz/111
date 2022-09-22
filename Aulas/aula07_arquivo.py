
lista = ["aaa","bbb","ccc"]
lista2= [111,222,333,444]

d = {"a":"Abacate", "b":"Berita", "c":"Cerveja"}

# # Abrir / ou criar o arquivo
# arq = open("meu_arquivo.txt","w")  # w-Escrita/Criar   r-Leitura    a-Adicionar
# # manipular conteúdo
#
# arq.write("linha 1"+"\n")
# arq.write("linha 2\n")
# arq.write("linha 3"+"\n")
#
# for x in range(4):
#     arq.write(input(">>:: ")+"\n")
#
# for x in lista:
#     arq.write(x+"\n")
#
# arq.writelines(lista)
# arq.writelines("\n")
# arq.writelines(str(lista2))
#
# arq.writelines("\n")
# arq.writelines(str(d.items()))
#
# arq.write("\n"+str(d))
#
# print("asfasdf",file=arq)
#
#
# # Fechar
# arq.close()


arq = open("meu_arquivo.txt","a")
arq.write("\n ==== E tenho dito ====")
arq.close()


a = open("meu_arquivo.txt","r")
for x in a:
    print(x)
a.close()

