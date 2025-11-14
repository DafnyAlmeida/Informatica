from funcoes import *

lista = []
pedidos = []

while True:
    print('''
        1 - Ver cardápio
        2 - Adicionar item ao pedido
        3 - Ver pedido
        4 - Remover item
        0 - Finalizar
          ''')
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        exibir_cardapio(lista)
    if opcao == "2":
        adicionar_pedido(lista, pedidos)
    if opcao == "3":
        exibir_pedido(pedidos)
    if opcao == "4":
        remover_item(pedidos)
    if opcao == "0":
        print("Obrigada por usar!")
        break