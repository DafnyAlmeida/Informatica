def carregar_cardapio(cardapio):
    while True:
        try:
            id = int(input("Digite o id do item: "))
        except ValueError:
            print("Id inválido")
            continue

        if any(item["Id"] == id for item in cardapio):
            print("Id já existente, tente novamente.")
        else:  
            break

        print("Id já existente, tente novamente.")

    nome = input("Digite o nome do item: ")
    preco = float(input("Digite o preço do item: "))
    
    item = {
        "Id": id, 
        "Nome": nome, 
        "Preço": preco
    }
    
    cardapio.append(item)
    print("Item adicionado com sucesso!")
    
def remover_item(cardapio):
    id_remover = int(input("Digite o id do item que deseja remover: "))
    for i in cardapio:
        if id_remover == i["Id"]:
            cardapio.remove(i)
    print("Item removido com sucesso!")