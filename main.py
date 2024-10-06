from modules import authors, publishers, books, loans

def menu():
    while True:
        print("\nMenu:")
        print("1. Autores")
        print("2. Editoras")
        print("3. Livros")
        print("4. Empréstimos")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            authors_menu()
        elif choice == "2":
            publishers_menu()
        elif choice == "3":
            books_menu()
        elif choice == "4":
            loans_menu()
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def authors_menu():
    while True:
        print("\nAutores:")
        print("1. Adicionar")
        print("2. Atualizar")
        print("3. Deletar")
        print("4. Listar")
        print("5. Buscar por Nome")
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            authors.add_author()
        elif choice == "2":
            authors.update_author()
        elif choice == "3":
            authors.delete_author()
        elif choice == "4":
            authors.list_authors()
        elif choice == "5":
            authors.find_author_by_name()
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def publishers_menu():
    while True:
        print("\nEditoras:")
        print("1. Adicionar")
        print("2. Atualizar")
        print("3. Deletar")
        print("4. Listar")
        print("5. Buscar por Nome")
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            publishers.add_publisher()
        elif choice == "2":
            publishers.update_publisher()
        elif choice == "3":
            publishers.delete_publisher()
        elif choice == "4":
            publishers.list_publishers()
        elif choice == "5":
            publishers.find_publisher_by_name()
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def books_menu():
    while True:
        print("\nLivros:")
        print("1. Adicionar")
        print("2. Atualizar")
        print("3. Deletar")
        print("4. Listar")
        print("5. Buscar por Título")
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            books.add_book()
        elif choice == "2":
            books.update_book()
        elif choice == "3":
            books.delete_book()
        elif choice == "4":
            books.list_books()
        elif choice == "5":
            books.find_book_by_title()
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def loans_menu():
    while True:
        print("\nEmpréstimos:")
        print("1. Adicionar")
        print("2. Atualizar")
        print("3. Deletar")
        print("4. Listar")
        print("5. Buscar por Status")
        print("0. Voltar")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            loans.add_loan()
        elif choice == "2":
            loans.update_loan()
        elif choice == "3":
            loans.delete_loan()
        elif choice == "4":
            loans.list_loans()
        elif choice == "5":
            loans.find_loan_by_status()
        elif choice == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
