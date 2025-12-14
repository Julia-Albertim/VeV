import pytest
from models.user import User
from models.user_system import UserSystem

# --- Testes para a classe User ---

@pytest.mark.parametrize("email, expected", [
    ("teste@dominio.com", True),
    ("outro.teste@sub.dominio.br", True),
    ("invalido@", False),
    ("invalido.com", False),
    ("@invalido.com", False),
    ("invalido@.com", False),
])
def test_user_is_valid_email(email, expected):
    """Testa a validação de formato de e-mail."""
    user = User("Nome", email, "senha123")
    assert user.is_valid_email() == expected

@pytest.mark.parametrize("password, expected", [
    ("senha123", True),  # Válida: >= 6 chars e dígito
    ("123456", True),    # Válida: apenas dígitos (>= 6 chars)
    ("abcde1", True),    # Válida: 6 chars e dígito
    ("abcde", False),    # Inválida: < 6 chars
    ("abcdef", False),   # Inválida: >= 6 chars, mas sem dígito
    ("s3nha", False),    # Inválida: < 6 chars
])
def test_user_is_strong_password(password, expected):
    """Testa a validação de senha forte (>= 6 chars e pelo menos um dígito)."""
    user = User("Nome", "email@teste.com", password)
    assert user.is_strong_password() == expected

# --- Testes para a classe UserSystem ---

@pytest.fixture
def user_system():
    """Fixture para criar uma instância limpa de UserSystem para cada teste."""
    return UserSystem()

def test_user_system_registrar_user_sucesso(user_system):
    """Testa o registro bem-sucedido de um novo usuário."""
    user = user_system.registrar_user("Alice", "alice@teste.com", "SenhaForte1")
    assert user.name == "Alice"
    assert user_system.total_users() == 1

def test_user_system_registrar_user_email_invalido(user_system):
    """Testa a falha de registro com e-mail inválido."""
    with pytest.raises(ValueError) as excinfo:
        user_system.registrar_user("Bob", "bob_invalido", "SenhaForte1")
    assert "E-mail inválido" in str(excinfo.value)
    assert user_system.total_users() == 0

def test_user_system_registrar_user_senha_fraca(user_system):
    """Testa a falha de registro com senha fraca."""
    with pytest.raises(ValueError) as excinfo:
        user_system.registrar_user("Charlie", "charlie@teste.com", "fraca")
    assert "Senha fraca" in str(excinfo.value)
    assert user_system.total_users() == 0

def test_user_system_encontrar_user_por_email(user_system):
    """Testa a busca de usuário por e-mail."""
    user_system.registrar_user("David", "david@teste.com", "SenhaForte1")
    
    # Encontrar usuário existente
    found_user = user_system.encontrar_user_por_email("david@teste.com")
    assert found_user is not None
    assert found_user.name == "David"
    
    # Não encontrar usuário inexistente
    not_found_user = user_system.encontrar_user_por_email("naoexiste@teste.com")
    assert not_found_user is None

def test_user_system_total_users(user_system):
    """Testa a contagem total de usuários."""
    assert user_system.total_users() == 0
    user_system.registrar_user("Eve", "eve@teste.com", "SenhaForte1")
    assert user_system.total_users() == 1
    user_system.registrar_user("Frank", "frank@teste.com", "SenhaForte2")
    assert user_system.total_users() == 2

# Teste de falha de lógica (F2 do relatório V&V): O sistema permite e-mails duplicados
def test_user_system_registrar_user_email_duplicado_falha_logica(user_system):
    """
    Testa a falha de lógica: o sistema atual permite o registro de e-mails duplicados.
    Este teste passa, mas em um sistema real, deveria falhar (ou seja, levantar uma exceção).
    """
    user_system.registrar_user("Grace", "grace@teste.com", "SenhaForte1")
    # Tenta registrar o mesmo e-mail novamente
    user_system.registrar_user("Grace Duplicada", "grace@teste.com", "OutraSenha1")
    
    # O total de usuários é 2, confirmando a falha de lógica (F2)
    assert user_system.total_users() == 2
    
    # A busca pelo e-mail retorna o primeiro usuário cadastrado (comportamento não determinístico)
    found_users = [u for u in user_system.users if u.email == "grace@teste.com"]
    assert len(found_users) == 2
