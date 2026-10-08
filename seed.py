from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    autor1 = Autor(
        nome="Machado de Assis",
        pais="Brasil"
    )

    autor2 = Autor(
        nome="Jorge Amado",
        pais="Brasil"
    )

    autor3 = Autor(
        nome="J. K. Rowling",
        pais="Reino Unido"
    )

    session.add(autor1)
    session.add_all([autor2, autor3])
    session.commit()

    # TODO: crie pelo menos 6 livros.
        livro1 = Livro(
        titulo="Dom Casmurro",
        ano=1899,
        autor_id=autor1.id,
        disponivel=True
    )

    livro2 = Livro(
        titulo="Memórias Póstumas de Brás Cubas",
        ano=1881,
        autor_id=autor1.id,
        disponivel=False
    )

    livro3 = Livro(
        titulo="Capitães da Areia",
        ano=1937,
        autor_id=autor2.id,
        disponivel=True
    )

    livro4 = Livro(
        titulo="Gabriela, Cravo e Canela",
        ano=1958,
        autor_id=autor2.id,
        disponivel=False
    )

    livro5 = Livro(
        titulo="Harry Potter e a Pedra Filosofal",
        ano=1997,
        autor_id=autor3.id,
        disponivel=True
    )

    livro6 = Livro(
        titulo="Harry Potter e a Câmara Secreta",
        ano=1998,
        autor_id=autor3.id,
        disponivel=False
    )

    session.add_all([
        livro1,
        livro2,
        livro3,
        livro4,
        livro5,
        livro6
    ])

    session.commit()
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    pass
