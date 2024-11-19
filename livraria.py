class Livro:
    def __init__(self, titulo, autor, genero, conteudo_magico):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.conteudo_magico = conteudo_magico

    def exibir_informacoes(self):
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Gênero: {self.genero}\n"
                f"Conteúdo Mágico: {self.conteudo_magico}\n")


class Catalogo:
    def __init__(self):
        self.lista_de_livros = []

    def adicionar_livro(self, livro):
        self.lista_de_livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado ao catálogo.")

    def ver_catalogo(self):
        print("Catálogo de Livros:")
        for livro in self.lista_de_livros:
            print(livro.exibir_informacoes())

    def buscar_por_titulo(self, titulo):
        for livro in self.lista_de_livros:
            if livro.titulo == titulo:
                print("Livro encontrado:")
                print(livro.exibir_informacoes())
                return
        print(f"O livro '{titulo}' não foi encontrado no catálogo.")

    def remover_livro(self, titulo):
        encontrado = False
        for livro in self.lista_de_livros:
            if livro.titulo == titulo:
                self.lista_de_livros.remove(livro)
                print(f"O livro '{titulo}' foi retirado do catálogo.")
                encontrado = True
                break
        if not encontrado:
            print(f"O livro '{titulo}' não foi encontrado no catálogo.")


class Bibliotecario:
    def __init__(self, nome, habilidades):
        self.nome = nome
        self.habilidades = habilidades

    def organizar_catalogo(self, catalogo):
        catalogo.lista_de_livros.sort(key=lambda livro: livro.titulo)
        print("O catálogo foi organizado em ordem alfabética pelo título.")

    def procurar_livro(self, catalogo, titulo):
        catalogo.buscar_por_titulo(titulo)

    def excluir(self, catalogo, titulo):
        catalogo.remover_livro(titulo)


class SistemaDeGestao:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def filtrar_por_genero(self, genero):
        print(f"Filtrando livros do gênero '{genero}':")
        encontrados = False
        for livro in self.catalogo.lista_de_livros:
            if livro.genero.lower() == genero.lower():
                print(livro.exibir_informacoes())
                encontrados = True
        if not encontrados:
            print(f"Nenhum livro do gênero '{genero}' foi encontrado.")


class Livraria:
    def __init__(self, nome, localizacao, sistema_de_gestao):
        self.nome = nome
        self.localizacao = localizacao
        self.sistema_de_gestao = sistema_de_gestao

    def integrar_livro(self, livro):
        self.sistema_de_gestao.catalogo.adicionar_livro(livro)

    def exibir_catalogo(self):
        self.sistema_de_gestao.catalogo.ver_catalogo()


def criar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    conteudo_magico = input("Digite o conteúdo mágico do livro: ")
    return Livro(titulo, autor, genero, conteudo_magico)


def menu():
    catalogo = Catalogo()
    sistema_de_gestao = SistemaDeGestao(catalogo)
    livraria = Livraria("Magic Books", "Programópolis", sistema_de_gestao)
    bibliotecario = Bibliotecario("Sr. Code", ["Organizar", "Buscar"])

    while True:
        print("***---Magic Books---***")
        print("1. Adicionar novo livro")
        print("2. Ver catálogo")
        print("3. Organizar catálogo")
        print("4. Buscar livro por título")
        print("5. Filtrar livros por gênero")
        print("6. Remover título")
        print("7. Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            livro = criar_livro()
            livraria.integrar_livro(livro)

        elif opcao == '2':
            livraria.exibir_catalogo()

        elif opcao == '3':
            bibliotecario.organizar_catalogo(catalogo)

        elif opcao == '4':
            titulo = input("Digite o título do livro que deseja buscar: ")
            bibliotecario.procurar_livro(catalogo, titulo)

        elif opcao == '5':
            genero = input("Digite o gênero dos livros que deseja filtrar: ")
            sistema_de_gestao.filtrar_por_genero(genero)

        elif opcao == '6':
            titulo = input("Digite o título do livro que deseja remover: ")
            bibliotecario.excluir(catalogo, titulo)

        elif opcao == '7':
            print("Fechando o sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


menu()
