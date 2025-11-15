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
    if opcao == "1":
        exibir_cardapio(lista)
    if opcao == "2":
        adicionar_pedido(lista, lista2)
    if opcao == "3":
        exibir_pedido(lista2)
    if opcao == "4":
        remover_item(lista2)
    if opcao == "5":
        carregar_cardapio(lista)
    if opcao == "0":
        print("Obrigada por usar!")
        break