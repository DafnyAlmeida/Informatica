# Questão 11 – Função calculadora
def calculadora():
    print("Essa é uma calculadora!")
    print("Menu:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    opera = int(input("Digite a operação (1, 2, 3, 4): "))

    if opera == 1:
        resultado = n1 + n2
    if opera == 2:
        resultado = n1 - n2
    if opera == 3:
        resultado = n1 * n2
    if opera == 4:
        if n2 == 0:
            print("Erro: operação invalida")
            return
        resultado = n1 / n2
    else:
        print("Operação invalida")
        return
    print(f"O resultado é {resultado}")

calculadora()

# Questão 12 – Verificar primo
def primo(n):
     if n < 2:
        print("Não é primo")
        return
     for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Não é primo")
            return
        
        print("É primo")
primo(1)


# Questão 13 – Inverter palavra
def invertida(palavra):
    resultado = palavra[::-1]
    print(f"{palavra} de tras para frente é {resultado}")
invertida("Tacocat")


# Questão 14 – Contar pares e ímpares
pares = 0
impares = 0
for n in range(1, 10 + 1):
    num = int(input(f"Digite o número {n}: "))
    if num % 2 == 0:
        pares += 1
    if num % 2 != 0:
        impares += 1
print(f"Dos número digitado {pares} são pares e {impares} são ímpares")

# Questão 15 – Sequência de Fibonacci
def fibonacci(n):
    a, b = 0, 1 # O a é 0 e o b é 1
    resultado = []
    while a <= n:
        resultado.append(a)
        a, b = b, b + a # aqui o a passa a ser 1 e o b passa a ser 1
    print(f"A sequecia de Fibonacci até esse número é {resultado}")
fibonacci(20)
