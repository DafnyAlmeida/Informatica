# q11
print("Essa é a função calculadora!")
print("0 - sair, 1 - adição, 2 - subtração, 3 - multipl1icação, 4 - divisão")
def calculadora(n1, n2, opera):
    if opera == 1:
        print(f"O resultado da soma é : {n1 + n2}")
    if opera == 2:
        print(f"O resultado da subtração é : {n1 - n2}")
    if opera == 3:
        print(f"O resultado da multiplicação é : {n1 * n2}")
    if opera == 4: 
        print(f"O resultado da divisão é : {n1 / n2}")
    if opera == 0:

calculadora(100, 2, 4)