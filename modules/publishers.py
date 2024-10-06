from bson import ObjectId
from database import get_db
from utils import input_with_validation

db = get_db()
publishers = db.publishers

def add_publisher():
    name = input("Nome da Editora: ")
    country = input("País da Editora: ")
    publishers.insert_one({"nome": name, "país": country})
    print("Editora adicionada com sucesso.")

def update_publisher():
    publisher_id = input("ID da Editora a ser atualizada: ")
    publisher = publishers.find_one({"_id": ObjectId(publisher_id)})
    if not publisher:
        print("Editora não encontrada.")
        return

    name = input(f"Novo nome da Editora ({publisher['nome']}): ")
    country = input(f"Novo país da Editora ({publisher['país']}): ")
    publishers.update_one({"_id": ObjectId(publisher_id)}, {"$set": {"nome": name, "país": country}})
    print("Editora atualizada com sucesso.")

def delete_publisher():
    publisher_id = input("ID da Editora a ser deletada: ")
    publishers.delete_one({"_id": ObjectId(publisher_id)})
    print("Editora deletada com sucesso.")

def list_publishers():
    for publisher in publishers.find():
        print(f"ID: {publisher['_id']}, Nome: {publisher['nome']}, País: {publisher['país']}")

def find_publisher_by_name():
    name = input("Nome da Editora a ser pesquisada: ")
    publisher = publishers.find_one({"nome": name})
    if publisher:
        print(f"ID: {publisher['_id']}, Nome: {publisher['nome']}, País: {publisher['país']}")
    else:
        print("Editora não encontrada.")
