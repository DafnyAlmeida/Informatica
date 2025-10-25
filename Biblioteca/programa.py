from funcoes import *

livros = []

while True:
    print("Bem-vindo a sua biblioteca")
    print("Aqui estão suas opções:")
    print("1 - Adicionar livro")
    print("2 - Exibir todos os livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1: 
        adicionar_livro(livros)
    if opcao == 2:
        exibir_livros(livros)
    if opcao == 3:
        emprestar_livro(livros)
    if opcao == 4:
        devolver_livro(livros)
    if opcao == 0:
        print("Biblioteca encerrada, até mais! \U0001f609 \U0001fae6")
        break
    if opcao not in [1, 2, 3, 4, 0]:
        print("Opção inválida, tente novamente \U0001f615")