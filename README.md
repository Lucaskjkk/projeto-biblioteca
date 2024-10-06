Nome do Sistema:

Gestão de Biblioteca

Assunto Abordado:

O sistema será voltado para a gestão de uma biblioteca, permitindo a administração de livros, autores, editoras e o controle de empréstimos.



Modelagem das Coleções
Autores (authors)

_id (ObjectId)
nome (string)
nacionalidade (string)
----------------------------------------------------------
Editoras (publishers)

_id (ObjectId)
nome (string)
país (string)
----------------------------------------------------------
Livros (books)

_id (ObjectId)
título (string)
autor_id (ObjectId, referência à coleção authors)
editora_id (ObjectId, referência à coleção publishers)
ano_publicacao (int)
----------------------------------------------------------
Empréstimos (loans)

_id (ObjectId)
livro_id (ObjectId, referência à coleção books)
data_emprestimo (date)
data_devolucao (date)
status (string, "emprestado" ou "devolvido")
----------------------------------------------------------
