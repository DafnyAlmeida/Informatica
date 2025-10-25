from tabulate import tabulate
# import emoji

def adicionar_livro(listaLivros):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    
    for livro in listaLivros:
        if livro["Título"].lower().strip() == titulo.lower().strip() and livro["Autor"].lower().strip() == autor.lower().strip():
            print("Esse livro já foi cadastrado")
            return

    livro = {
        "Título": titulo, 
        "Autor": autor,
        "Status": "Disponível" 
    }
    
    listaLivros.append(livro)
    print("Livro cadastrado com sucesso \u2705")
    return

def emprestar_livro(listaLivros):
    titulo = input("Digite o título do livro que deseja retirar: ").lower()
    for livro in listaLivros:
        if titulo.lower().strip() == livro["Título"].lower().strip():
            if livro["Status"] == "Disponível":
                livro["Status"] = "Emprestado"
                print("Livro retirado com sucesso")
                return
            if livro["Status"] == "Emprestado":
                print("Livro não disponível no momento")
                return
        if livro not in listaLivros: 
            print("\U0001f6a8 Livro não cadastrado")
            return

def devolver_livro(listaLivros):
    titulo = input("Digite o título do livro que deseja devolver: ")
    for livro in listaLivros:
        if titulo.lower().strip() == livro["Título"].lower().strip():
            if livro["Status"] == "Emprestado":
                livro["Status"] = " Disponível"
                print("Livro devolvido com sucesso \u2705")
                return
            if livro["Status"] == "Disponível":
                print("O livro não foi emprestado, logo não pode ser devolvido")
                return
        if livro not in listaLivros: 
            print("\U0001f6a8 Livro não cadastrado")
            return

def exibir_livros(listaLivros):
    if not listaLivros:
        print("Nenhum livro cadastrado")
        return
    tabela = [[livro["Título"], livro["Autor"], livro["Status"]] for livro in listaLivros]
    print(tabulate(tabela, headers=["Título", "Autor", "Status"], tablefmt="fancy_grid"))
