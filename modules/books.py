from bson import ObjectId
from database import get_db
from utils import input_with_validation

db = get_db()
books = db.books

def add_book():
    title = input("Título do Livro: ")
    author_id = input("ID do Autor: ")
    publisher_id = input("ID da Editora: ")
    year = int(input("Ano de Publicação: "))

    books.insert_one({"título": title, "autor_id": ObjectId(author_id), "editora_id": ObjectId(publisher_id), "ano_publicacao": year})
    print("Livro adicionado com sucesso.")

def update_book():
    book_id = input("ID do Livro a ser atualizado: ")
    book = books.find_one({"_id": ObjectId(book_id)})
    if not book:
        print("Livro não encontrado.")
        return

    title = input(f"Novo título do Livro ({book['título']}): ")
    author_id = input(f"Novo ID do Autor ({book['autor_id']}): ")
    publisher_id = input(f"Novo ID da Editora ({book['editora_id']}): ")
    year = int(input(f"Novo ano de publicação ({book['ano_publicacao']}): "))

    books.update_one({"_id": ObjectId(book_id)}, {"$set": {"título": title, "autor_id": ObjectId(author_id), "editora_id": ObjectId(publisher_id), "ano_publicacao": year}})
    print("Livro atualizado com sucesso.")

def delete_book():
    book_id = input("ID do Livro a ser deletado: ")
    books.delete_one({"_id": ObjectId(book_id)})
    print("Livro deletado com sucesso.")

def list_books():
    for book in books.find():
        print(f"ID: {book['_id']}, Título: {book['título']}, Autor ID: {book['autor_id']}, Editora ID: {book['editora_id']}, Ano de Publicação: {book['ano_publicacao']}")

def find_book_by_title():
    title = input("Título do Livro a ser pesquisado: ")
    book = books.find_one({"título": title})
    if book:
        print(f"ID: {book['_id']}, Título: {book['título']}, Autor ID: {book['autor_id']}, Editora ID: {book['editora_id']}, Ano de Publicação: {book['ano_publicacao']}")
    else:
        print("Livro não encontrado.")
