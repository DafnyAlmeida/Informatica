# # Questão 01 - Cadastro de nomes
# lista = []
# cont = 0
# for i in range(0, 5):
#     n = input("Digite um nome: ").lower()
#     lista.append(n)
# for nome in lista:
#     if nome[0] == "a":
#         cont += 1
# print(f"A lista é a seguinte: {lista} e {cont} nomes começam com 'a'")



# Questão 02 - Média de notas com função
# lista = []
# for i in range(1, 6):
#     n = int(input(f"Digite a {i}º nota: "))
#     lista.append(n)
# def media(lista):
#     media = sum(lista)/5
#     if media >= 7:
#         print(f"A media foi {media} e você foi aprovado")
#     else: 
#         print(f"A media foi {media} e você foi reprovado")
# media(lista)


# # Questão 03 - Busca em lista 
# lista = []
# for i in range(0, 6):
#     n = int(input("Digite um número: "))
#     lista.append(n)

# opcao = input("Deseja ver se algum número esta na lista (s/n): ")
# if opcao == "s":
#     nu = int(input("Digite o número: "))
#     if nu in lista:
#         print(f"A lista é {lista} e {nu} já esta presente na posição {lista.index(nu)}")
#     else:
#         print(f"A lista é {lista} e {nu} não esta presente")
# else: 
#     print("Programa encerrado")


# # Questão 04
# lista = []
# lista_pares = []
# for i in range(10):
#     n = int(input("Digite um número: "))
#     lista.append(n)
# def filtrar_pares():
#     for b in lista:
#         if b % 2 == 0:
#             lista_pares.append(b)
# filtrar_pares()
# print(f"A lista tem os seguintes itens: {lista} sendo os pares os seguintes: {lista_pares}")


# # Questão 05
# lista = []
# for i in range(8):
#     n = int(input("Digite um número: "))
#     lista.append(n)
# print(f"O maior número da lista é: {max(lista)}")
# print(f"O menor número da lista é: {min(lista)}")
# print(f"A soma de todos os números é: {sum(lista)}")
# print(f"A média dos números é: {sum(lista)/8}")


# # Questão 06
# lista = []
# for i in range(10):
#     n = int(input("Digite um número: "))
#     lista.append(n)

# def remover(lista, valor):
#     lista.remove(valor)
#     print(f"A nova lista é: {lista}")

# opcao = input("Deseja remover um valor (s/n): ")
# if opcao == "s":
#     valor = int(input("Digite o valor a ser removido: "))
#     remover(lista, valor)
# else:
#     print("Programa encerrado")


# # Questão 07
# lista = []
# for i in range(5):
#     n = input("Digite o nome do convidado: ")
#     lista.append(n)
# opcao = input("Deseja ver se algum convidado já esta na lista (s/n): ")
# if opcao == "s":
#     valor = input("Digite o nome: ")
#     if valor in lista: 
#         print("Convidado encontrado!")
#     else:
#         print("Convidado não encontrado!")
#         opcao1 = input("Deseja adicionalo a lista (s/n): ")
#         if opcao1 == "s":
#             print("Feito!")
#             lista.append(valor)
# else:
#     print("Programa encerrado")


# # Questão 08
# lista = []
# acima = []
# for i in range(6):
#     n = int(input("Digite a nota: "))
#     lista.append(n)
#     media = sum(lista)/6
#     if n >= 6:
#         acima.append(n)
# print(f"A media dos números é {media} e os seguintes números estão acima da média {acima}")


# # Questão 09
# lista = []
# for i in range(5):
#     p = input("Digite o nome do produto: ")
#     lista.append(p)
# print(f"A lista é a seguinte {lista}")
# opcao = input("Deseja remover algum produto (s/n): ")
# if opcao == "s":
#     valor = input("Digite o nome do produto: ")
#     lista.remove(valor)
#     print(f"A lista atualizada é {lista}")
# else:
#     print("Programa encerrado")


# # Questão 10
# def filtar_nomes(lista):
#     for i in lista:
#         if len(i) >= 5:
#             lista_filtrada.append(i)
#     print(f"A lista é {lista_filtrada}")

# lista = []
# lista_filtrada = []
# for i in range(7):
#     n = input("Digite o nome: ")
#     lista.append(n)

# filtar_nomes(lista)