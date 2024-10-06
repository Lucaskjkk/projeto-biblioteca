from bson import ObjectId
from database import get_db
from utils import input_with_validation

db = get_db()
authors = db.authors

def add_author():
    name = input("Nome do Autor: ")
    nationality = input("Nacionalidade do Autor: ")
    authors.insert_one({"nome": name, "nacionalidade": nationality})
    print("Autor adicionado com sucesso.")

def update_author():
    author_id = input("ID do Autor a ser atualizado: ")
    author = authors.find_one({"_id": ObjectId(author_id)})
    if not author:
        print("Autor não encontrado.")
        return

    name = input(f"Novo nome do Autor ({author['nome']}): ")
    nationality = input(f"Nova nacionalidade do Autor ({author['nacionalidade']}): ")
    authors.update_one({"_id": ObjectId(author_id)}, {"$set": {"nome": name, "nacionalidade": nationality}})
    print("Autor atualizado com sucesso.")

def delete_author():
    author_id = input("ID do Autor a ser deletado: ")
    authors.delete_one({"_id": ObjectId(author_id)})
    print("Autor deletado com sucesso.")

def list_authors():
    for author in authors.find():
        print(f"ID: {author['_id']}, Nome: {author['nome']}, Nacionalidade: {author['nacionalidade']}")

def find_author_by_name():
    name = input("Nome do Autor a ser pesquisado: ")
    author = authors.find_one({"nome": name})
    if author:
        print(f"ID: {author['_id']}, Nome: {author['nome']}, Nacionalidade: {author['nacionalidade']}")
    else:
        print("Autor não encontrado.")
