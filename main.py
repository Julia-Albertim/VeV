from models.user_system import UserSystem

def exibir_menu():
    print("\n=== SISTEMA DE USUÁRIOS ===")
    print("1 - Cadastrar usuário")
    print("2 - Buscar usuário por e-mail")
    print("3 - Listar todos os usuários")
    print("4 - Sair")

def cadastrar_usuario(us):
    print("\n--- Cadastro de Usuário ---")
    name = input("Nome: ")
    email = input("E-mail: ")
    password = input("Senha: ")

    try:
        us.registrar_user(name, email, password)
        print("Usuário cadastrado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def buscar_usuario(us):
    print("\n--- Buscar Usuário ---")
    email = input("Digite o e-mail: ")

    user = us.encontrar_user_por_email(email)
    if user:
        print(f"Usuário encontrado: {user.name} | {user.email}")
    else:
        print("Usuário não encontrado.")

def listar_usuarios(us):
    print("\n--- Usuários Cadastrados ---")
    if not us.users:
        print("Nenhum usuário cadastrado.")
        return
    
    for idx, user in enumerate(us.users, start=1):
        print(f"{idx}. {user.name} - {user.email}")

def iniciar_interface():
    us = UserSystem()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(us)
        elif opcao == "2":
            buscar_usuario(us)
        elif opcao == "3":
            listar_usuarios(us)
        elif opcao == "4":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar_interface()