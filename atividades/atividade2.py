# Questão 01
media = 0
for i in range(3):
    notas = float(input("Digite sua nota: "))
    media += notas
media = media/3
print(f"Sua média foi de: {media:.2f}")

# Questão 02
palavra = input("Diga-me uma palavra: ")
contador = 0
vogais = "aeiouAEIOU"
for l in palavra:
    if l in vogais:
        contador += 1
print(f"A sua palavra tem {contador} vogais")

# Questão 03
while True:
    n = float(input("Me diga um número (digite 0 para parar): "))
    if n == 0:
        break
    elif n % 2 == 0:
        print(f"{n} é par")
    else:
        print(f"{n} é ímpar")

# Questão 04
for i in range (5):
    n = int(input("Diga-me um número: "))
    if i == 0:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f"O menor número digitado é: {menor} e o maior é: {maior}")

# Questão 05
total = 0
maior = 0
lista = []
while True:
    preco = int(input("Digite o preço do produto (digite 0 para parar): "))
    total += preco
    if preco == 0:
        print(f"O total foi de: {total}")
        break
    if preco >= 100:
        maior += 1
        lista.append(preco)
print(f"{maior} são maiores ou iguais a 100, sendo eles {lista}")

# Questão 06
n = int(input("Digite o número que deseja saber o fatorial: "))
resultado = 1
for i in range(1, n + 1): #Range não aceita float
    resultado *= i
print(f'O fatorial do número {n} é: {resultado}')