# Questão  - Maior de vários números
# while True:
#     numeros = float(input("Digite um número ou 0 para sair: "))
#     maior = numeros[0] 
#     menor = numeros[0]
#     if numeros > maior:
#         maior = numeros
#     if numeros < menor:
#             menor = numeros
#     if numeros == 0:
#         break 

# # Questão 01 - Maior de três números
# for n in range(1, 3 + 1):
#     numeros = int(input("Digite um número: "))
#     if n == 1:
#         maior = menor = numeros
#     if numeros > maior:
#         maior = numeros
#     if numeros < menor:
#         menor = numeros
# print(f"O maior número é {maior} e o menor é {menor}")

# # Questão 02 - Lançar!
# for i in range(10, -1, -1): #range(start, stop, step) onde o start é de onde começa, o stop é onde para e o step é o passo
#     print(f"Contagem regressiva: {i}")
# print("Lançar")

# # Questão 03 - Lista de compras 
# lista = []
# while True:
#     produ = input("Digite o produto ou sair para parar: ")
#     if produ.lower().replace(" "," ") != "sair":
#         lista.append(produ)
#     if produ.lower().replace(" "," ") == "sair":
#         print(f"Os produtos listados foram: {", ".join(lista)}")
#         break

# # Questão 04 - Números primos
# def primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#         else:
#             return True

# numero = int(input("Digite um número: "))
# if primo(numero):
#     print("É primo")
# else:
#     print("Não é primo")

# Questão 05 - Adivinhação
# from random import randint
# n = randint(1, 100)
# while True:
#     tentativa = int(input("Digite seu palpite: "))
#     if tentativa == n:
#         print('Parabéns você acertou!')
#         break
#     if tentativa > n:
#         print('Seu palpite é maior que o número')
#     if tentativa < n:
#         print('Seu palpite é menor que o número')

# # Questão 06 - Analisador de textos
# texto = input("Digite o texto a ser analisado: ")
# palavras = texto.split()
# qtd_palavras = len(palavras)
# vogais = "aeiou"
# texto_formatado = texto.lower().replace(" ", " ")
# qtd_vogais = 0
# consoantes = 0
# for letra in texto_formatado:
#     if letra in vogais:
#         qtd_vogais += 1
#     else:
#         consoantes += 1
# print(f"O text tem {qtd_palavras} palavras, {qtd_vogais} vogais e {consoantes} consoantes")

# def temperatura():
#     print("1 - Celsius pra Fahrenheit")
#     print("2 - Fahrenheit pra Kelvin")
#     print("3 - Celsius pra Kelvin")
#     opcao = int(input("Escolha: "))
#     t1 = float(input("Digite a temperatura: "))
#     if opcao == 1:
#         resultado = 1.8*t1 + 32
#         print(f"A temperatura é {resultado}")
#     if opcao == 2:
#         resultado2 = t1 + 459.67 * (5/9)
#         print(f"A temperatura é {resultado2}")
#     if opcao == 3:
#         resultado3 = t1 + 273
#         print(f"A temperatura é {resultado3}")
# temperatura()