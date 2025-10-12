# # Questão 01 - Cadastro de nomes
# lista_nomes = []
# nomes_a = []

# for n in range(1, 6):
#     nome = input(f"Digite o {n}º nome: ").strip()
#     lista_nomes.append(nome)
#     primeira = nome[0].lower()
#     if primeira != "a":
#         nomes_a.append(nome)
# cont = len(nomes_a)
# print(f"Dos nomes digitados {cont} não começam com a letra 'a', sendo eles: {nomes_a}")  


# # Questão 02 - Média de notas 
# lista_notas = []
# def media(lista):
#     media = sum(lista)/4
#     print(f"A média é {media}")
#     if media >= 7:
#         print("Você foi aprovado!")
#     if media < 7:
#         print("Você foi reprovado!")

# for i in range(1, 5):
#     nota = int(input(f"Digite a {i}º nota: "))
#     lista_notas.append(nota)
# media(lista_notas)


# # Questão 03 - Soma de pares e ímpares
# lista = []
# soma_pares = 0
# soma_impares = 0
# for i in range(1, 11):
#     n = int(input(f"Digite o {i}º número: "))
#     lista.append(n)
# for item in lista:
#     if item % 2 == 0:
#         soma_pares += item
#     else:
#         soma_impares += item
# print(f"A lista tem os seguintes números {lista}, a soma dos pares é {soma_pares} e dos ímpares é {soma_impares}")


# Questão 04 - Lista de convidados 
# lista_convidados = []
# for i in range(1, 6):
#     convidado = input("Digite o nome do convidado: ")
#     lista_convidados.append(convidado)
# while True:
#     opcao = input("Deseja verificar se um nome esta na lista (s/n/parar): ")
#     if opcao == "s":
#         verificar = input("Digite o nome do convidado: ")
#         if verificar in lista_convidados: 
#             print("O convidado está na lista")
#         else: 
#             print("O convidado não está na lista")
#             opcao1 = input("Deseja adiciona-lo? (s/n)")
#             if opcao1 == "s":
#                 lista_convidados.append(verificar)
#                 print("Feito!")
#             else:
#                 print("Certo")
#     if opcao == "sair":
#         break
#     else:
#         print("Programa encerrado")


# # Questão 05 - Nomes com mais de 5 letras
# lista_nomes = []

# for n in range(1, 8):
#     nome = input(f"Digite o {n}º nome: ").strip()
#     lista_nomes.append(nome)

# def filtra_nomes(lista):
#     lista_filtro = []
#     for nome in lista:
#         if len(nome) >= 5:
#             lista_filtro.append(nome)
#     print(f"A lista original era: {lista} e depois do filtro passou a ser: {lista_filtro}")
# filtra_nomes(lista_nomes)

# # Questão 06 - Busca por posição
# lista_num = []

# for n in range(1, 7):
#     num = int(input(f"Digite o {n}º número: "))
#     lista_num.append(num)
# posi = int(input("Digite uma posição para buscar na lista: "))
# num_posi = lista_num[posi]
# if len(lista_num) - 1 < posi:
#     print("Posição invalida")
# else:
#     print(f"O número na posição {posi} é {num_posi}")


# # Questão 07 - Par ou ímpar
# def par_impar(n):
#     if n % 2 == 0:
#         print(f"{n} é par")
#     if n % 2 != 0:
#         print(f"{n} é ímpar")

# n = int(input("Digite um número: "))
# par_impar(n)

# # Questão 08 - Contagem regressiva
# for i in range(10, -1, -1):
#     print(i)
# print("Explosão!")