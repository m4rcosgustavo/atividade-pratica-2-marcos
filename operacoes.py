from sqlalchemy import select

from models import Livro


def emprestar_livro(session, titulo):
    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )
    # TODO: se o livro não existir, exiba uma mensagem.
    if livro is None:
        print("Livro não encontrado.")
        return
    # TODO: se já estiver indisponível, exiba uma mensagem.
    if not livro.disponivel:
        print("Livro indisponível.")
        return
    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    livro.disponivel = False
    session.commit()

    print("Livro emprestado com sucesso.")
    pass


def devolver_livro(session, titulo):
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    livro = session.scalar(
        select(Livro).where(Livro.titulo == titulo)
    )

    # TODO: se o livro não existir, exiba uma mensagem.
    if livro is None:
        print("Livro não encontrado.")
        return
    # TODO: se já estiver disponível, exiba uma mensagem.
    if livro.disponivel:
        print("O livro já está disponível.")
        return
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    livro.disponivel = True
    session.commit()

    print("Livro devolvido com sucesso.")
    pass
