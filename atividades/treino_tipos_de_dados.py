# Questões set
# conjunto = {1, 2, 3}
# conjunto.add(4)
# conjunto.remove(2)
# print(conjunto)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# uniao = set1.union(set2)
# print(uniao) # Perceba que ele não repete o que tem nos dois

# interse = set1.intersection(set2)
# print(interse)

# diferenca = set2.difference(set1)
# print(diferenca) #Ele só ira printar o que o primeiro tem de diferente

# frase = input("Digite uma frase: ")
# letras_unicas = set(frase.lower().replace(" ", " "))
# if " " in letras_unicas:
#     letras_unicas.remove(" ")
# print(letras_unicas)

# from random import randint
# set1 = set()
# while len(set1) < 10:
#     n = randint(1, 100)
#     set1.add(n)
# print(set1)

# Questões Dict
# dicio = {"Nome": "Dafny", "idade": 15, "curso": "Informática"}
# print(dicio.keys())
# print(dicio.values())
# print(dicio.items())
# dicio["nota"] = 10
# print(dicio)

# def mercado():
#     dic_mercado = {}
#     total = 0

#     while True:
#         chave = input("Digite o nome do produto ou sair para parar: ").lower()
#         if chave == "sair":
#             break

#         valor = float(input("Digite o valor do produto: "))
#         total += valor
#         dic_mercado[chave] = valor

#     if dic_mercado:
#         produto_maior_valor = max(dic_mercado, key=dic_mercado.get)
#         mais_caro = dic_mercado[produto_maior_valor]
#         print(f"O total foi de {total}")
#         print(f"Você comprou {len(dic_mercado)} produtos sendo eles os seguintes: {dic_mercado.keys()}, sendo o mais caro {produto_maior_valor} com valor de {mais_caro}")

#     while True:
#         opcao = input("Deseja consultar a preço de algum produto (s/n): ")
#         if opcao == "s":
#             produto = input("Digite o nome do produto: ").lower()
#             if produto in dic_mercado:
#                 print(f"O preço do {produto} é R$ {dic_mercado[produto]:.2f}")
#         if opcao == "n": 
#             break

# mercado()