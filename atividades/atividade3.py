# Questão 1 - Indicador de IMC
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = round(peso/altura**2, 1)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")

# Questão 2 - Indica se um número é impar ou par
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é ímpar")

# Questão 3 - Tabuada
n = int(input("Digite um número: "))
for i in range (1, 11):
    print(f"{i} X {n} = {n * i}")

# Questão 4 - Checa se um número é primo
n = int(input("Digite um número: "))
raiz_n = int(round(n ** 0.5 + 1))
eh_primo = True
for i in range(2, raiz_n):
    if n % i == 0:
        eh_primo = False
        break
if eh_primo and n > 1:
    print(f"{n} é primo")
else:
     print(f"{n} não é primo")

# Questão 5 - Notas de uma turma
n = int(input("Digite o número de alunos na turma: "))
abaixo = acima = notas = 0
for i in range(1, n + 1):
    nota = int(input(f"Digite a nota do aluno {i}: "))
    notas += nota
    if nota < 6:
        abaixo += 1
    elif nota <= 6:
        acima += 1
media = round(notas/n, 2)
print(f"A média da turma foi {media}, {abaixo} alunos ficaram abaixo da média e {acima} alunos ficaram acima da média")

# Questão 6 - Número secreto
from random import randint
n = randint(1, 20)
print("Tente adivinhar o número secreto entre 1 e 20")
while True:
    user = int(input("Digite seu palpite: "))
    if n == user:
        print("Parabéns! Você acertou")
        break
    elif user > n:
        print("Seu chute foi maior que o número")
    elif user < n:
        print("Seu chute foi menor que o número")
    