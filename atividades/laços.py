#1 questão
for n in range(1,11):
    print(n)

#2 questao
n=10
while n != 0:
    print(n)
    n -=1

#3 questao
nome = input("qual o seu nome")
for n in range(5):
    print(nome)

#4 questao
for n in range(0, 21,2):
    print(n)

#5 questao
senha = 1234
while True:
    senha1 = int(input("Digite a senha: "))
    if senha1 == senha:
        print("Senha correta: ")
        break
    else:
        print("Senha incorreta: ")
        continue

#Questão 6
pedirN = 1
soma = 0
while pedirN <=5:
    numeros = float(input("Digite um número: "))
    pedirN += 1
    soma += numeros
    continue
print(f"A soma é {soma}")
   
#Questão 7
for n in range(1,11):
    if n % 2 == 0:
        print(n)

#Questão 8
n = []
while True:
    numeros = float(input("Digite uma lista de números, um por vez, e aperte 0 se quiser parar: "))
    if numeros == 0:
        break
    n.append(numeros)
print(f"Os números foram: {n}")

#Questão 9 
numero = float(input("Digite o número o qual deseja saber a tabuada: "))
for n in range(1,11):
    print(numero * n)

