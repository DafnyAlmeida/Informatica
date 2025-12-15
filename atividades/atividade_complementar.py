# # Questão 6
largura = int(input("Digite a largura da parede: "))
altura = int(input("Digite a altura da parede: "))
area = largura * altura
print(f"A área da parede é {area}")
litros = round(area/5, 2)
preco = litros * 25
print(f"O preço para pintar essa parede é de {preco}")

# # Questão 7
ano = int(input("Digite um ano: "))
if ano % 400 == 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} é normal")

# # Questão 8
print("A seguir digite o valor de cada produto da sua compra e aperte 0 se quiser parar")
compras = 0
while True:
    produto = int(input("Digite o valor: "))
    compras += produto
    if produto == 0:
        break
print (f"O preço total foi de {compras}")
print("Formas de pagamento: ")
opcao = int(input("[1] À vista dinheiro, [2] À vista no cartão, [3] Em até 2x no cartão, [4] 3x ou mais no cartão: "))
if opcao == 1:
    valor = compras * 0.1
elif opcao == 2:
    valor = compras * 0.05
elif opcao == 3:
    valor = compras
elif opcao == 4:
    valor = compras * 1.2
print(f"O valor a ser pago é {valor}")

# # Questão 9
valor = int(input("Digite o valor que deseja sacar: "))
cinquenta = valor // 50
modulo_cin = valor % 50
vinte = modulo_cin // 20
modulo_vin = modulo_cin % 20
dez = modulo_vin // 10
modulo_dez = modulo_vin % 10
um = modulo_dez // 1 
if cinquenta != 0:
    print(f"Você receberá {cinquenta} notas de R$50")
if vinte != 0:
    print(f"Você receberá {vinte} notas de R$20")
if dez != 0: 
    print(f"Você receberá {dez} notas de R$10")
if um != 0: 
    print(f"Você receberá {um} notas de R$1")

# Questão 12
par = 0
primos = 0
impar = 0
while True: 
    n = int(input("Digite um número e aperte 0 para parar: "))
    if n == 0:
        break
    if n % 2 == 0: 
        par += 1
    if n % 2 != 0: 
        impar += 1
    if n > 1:
        eh_primo = True
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos += 1
print(f"Você digitou {primos} números primos, {par} pares e {impar} ímpares")

