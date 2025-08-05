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

