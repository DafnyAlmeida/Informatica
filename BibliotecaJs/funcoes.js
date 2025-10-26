function adicionar_livro(listaLivros) {
    let titulo = prompt("Digite o título do livro");
    let autor = prompt("Digite o autor do livro");

    for (let livro in listaLivros) {
        if (titulo == livro["Título"] && autor == livro["Autor"]) {
            return alert("Livro já cadastrado")
        };
    };

    let livro = {
        Título: titulo, 
        Autor: autor,
        Status: "Disponível"
    };

    listaLivros.push(livro);
    return alert("Livro cadastrado com sucesso");
};

function emprestar_livro(listaLivros) {
    let titulo = prompt("Digite o livro que deseja retirar")

    for (let livro in listaLivros) {
        if (titulo == livro["Título"]) {
            if (livro("Status") == "Disponível") {
                livro["Status"] = "Emprestado"
                return alert("Livro retirado com sucesso");
            };

            if (livro["Status"] == "Emprestado") {
                return alert("Livro não disponível no momento");
            };
        };

        if (!listaLivros.includes(livro)) {
           return alert("Livro não cadastrado")
        };
    };
};

function devolver_livro(listaLivros) {
    let titulo = prompt("Digite o nome do livro que deseja devolver");

    for (let livro in listaLivros) {
        if (titulo == livro["Título"]) {
            if (livro["Status"] == "Emprestado") {
                livro["Status"] = "Disponível"
                return alert("Livro devolvido com sucesso")
            };

            if (livro["Status"] == "Disponível") {
                return alert("O livro não foi emprestado, logo não pode ser devolvido")
            };
        };

        if (!listaLivros.includes(livro)) {
           return alert("Livro não cadastrado")
        };
    };
};

function exibir_livros(listaLivros) {
    if (listaLivros.length === 0) {
        return alert("Nenhum livro cadastrado");
    };
};
