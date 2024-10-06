from bson import ObjectId
from datetime import datetime
from database import get_db
from utils import input_with_validation

db = get_db()
loans = db.loans

def add_loan():
    book_id = input("ID do Livro: ")
    loan_date = input("Data de Empréstimo (YYYY-MM-DD): ")
    return_date = input("Data de Devolução (YYYY-MM-DD): ")
    status = input_with_validation("Status (emprestado/devolvido): ", lambda x: x in ["emprestado", "devolvido"], "Status inválido.")

    loans.insert_one({"livro_id": ObjectId(book_id), "data_emprestimo": datetime.strptime(loan_date, "%Y-%m-%d"), "data_devolucao": datetime.strptime(return_date, "%Y-%m-%d"), "status": status})
    print("Empréstimo adicionado com sucesso.")

def update_loan():
    loan_id = input("ID do Empréstimo a ser atualizado: ")
    loan = loans.find_one({"_id": ObjectId(loan_id)})
    if not loan:
        print("Empréstimo não encontrado.")
        return

    book_id = input(f"Novo ID do Livro ({loan['livro_id']}): ")
    loan_date = input(f"Nova Data de Empréstimo ({loan['data_emprestimo'].date()}): ")
    return_date = input(f"Nova Data de Devolução ({loan['data_devolucao'].date()}): ")
    status = input_with_validation(f"Novo status ({loan['status']}): ", lambda x: x in ["emprestado", "devolvido"], "Status inválido.")

    loans.update_one({"_id": ObjectId(loan_id)}, {"$set": {"livro_id": ObjectId(book_id), "data_emprestimo": datetime.strptime(loan_date, "%Y-%m-%d"), "data_devolucao": datetime.strptime(return_date, "%Y-%m-%d"), "status": status}})
    print("Empréstimo atualizado com sucesso.")

def delete_loan():
    loan_id = input("ID do Empréstimo a ser deletado: ")
    loans.delete_one({"_id": ObjectId(loan_id)})
    print("Empréstimo deletado com sucesso.")

def list_loans():
    for loan in loans.find():
        print(f"ID: {loan['_id']}, Livro ID: {loan['livro_id']}, Data de Empréstimo: {loan['data_emprestimo'].date()}, Data de Devolução: {loan['data_devolucao'].date()}, Status: {loan['status']}")

def find_loan_by_status():
    status = input_with_validation("Status a ser pesquisado (emprestado/devolvido): ", lambda x: x in ["emprestado", "devolvido"], "Status inválido.")
    for loan in loans.find({"status": status}):
        print(f"ID: {loan['_id']}, Livro ID: {loan['livro_id']}, Data de Empréstimo: {loan['data_emprestimo'].date()}, Data de Devolução: {loan['data_devolucao'].date()}, Status: {loan['status']}")
