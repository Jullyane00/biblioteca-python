biblioteca = []
while True:
    print("SISTEMA DE BIBLIOTECA")
    print("*"*20)
    print("1 - Cadastrar Livro")
    print("2 - Listar Livro")
    print("3 - Pesquisar Livro")
    print("4 - Emprestar Livro")
    print("5 - Devolver Livro")
    print("6 - Sair do Sistema")
    print("*"*20)
    opcao = int(input("Digite a opção desejada:"))

    if opcao == 1:
        print("Cadastrar Livro")
        titulo = input("Digite o título do livro:")
        autor = input("Digite o autor do livro:")
        ano = int(input("Digite o ano do livro:"))
        biblioteca.append([titulo, autor, ano])
        print("Livro cadastrado com sucesso!")
        print("*"*20)

    elif opcao == 2:
        print("Listar Livros")
        if biblioteca:
            for livro in biblioteca:
                print("Título:", livro[0], "Autor:", livro[1], "Ano:", livro[2])
            print("Livros listados com sucesso!")
        else:
            print("Não há livros cadastrados!")
        print("*"*20)

    elif opcao == 3:
        print("Pesquisar Livro")
        titulo = input("Digite o título do livro:")
        encontrado = False
        for livro in biblioteca:
            if livro[0].lower() == titulo.lower():
                print("Título:", livro[0], "Autor:", livro[1], "Ano:", livro[2])
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado!")
        print("*"*20)
