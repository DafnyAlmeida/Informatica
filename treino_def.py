# # Questão 01 - def maior
# def maior(n1, n2, n3):
#     maior = n1
#     if n2 > maior:
#         maior = n2
#     if maior < n3:
#         maior = n3
#     print(f"O maior número é {maior}")
# maior(12, 24, 90)

# # Questão 02 - def palindromo
# def palindromo(palavra):
#     palavra = palavra.lower().replace(" ", " ")
#     if palavra == palavra[::-1]:
#         print(f"{palavra} é um palindromo")
#     else:
#         print(f"{palavra} não é um palindromo")
# palindromo("tacocat")

# # Questão 03 - def fatorial
# def fatorial(n):
#     fatorial1 = 1
#     for i in range(1, n + 1):
#         fatorial1 *= i
#     print(fatorial1)
# fatorial()

# # Questão 04 - Def media
# def notas():

#     def media():
#         n = int(input("Quantas notas você tem: "))
#         soma = 0
#         for i in range(1, n + 1):
#             nota = int(input(f"Digite a {i}º nota: "))
#             soma += nota 
#             media = soma/n
#         print(f"A média foi {media}")
    
#     def situacao():
#             if media < 6:
#                 print("Reprovado")
#             if media >= 6:
#                 print("Aprovado")

#     return media(), situacao()
    
# notas()

# Q