from funcoes import *

lista = []
lista2 = []

while True:
    print('''
        1 - Ver cardápio
        2 - Adicionar item ao pedido
        3 - Ver pedido
        4 - Remover item
        5 - Adicionar item ao cardapio
        0 - Finalizar
          ''')
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            exibir_cardapio(lista)
        case "2":
            adicionar_pedido(lista, lista2)
        case "3":
            exibir_pedido(lista2)
        case "4":
            remover_item(lista2)
        case "5":
            carregar_cardapio(lista)
        case "0":
            print("Obrigada por usar!")
            break
        case _:
            print("Valor inválido, tente novamente")