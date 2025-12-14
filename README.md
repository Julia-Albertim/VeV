# Sistema Básico de Gerenciamento de Usuários

Sistema básico de gerenciamento de usuários em Python

## Estrutura do Projeto

*   `main.py`: Interface de linha de comando (CLI) para interagir com o sistema.
*   `models/user.py`: Classe `User` com lógica de validação de e-mail e senha.
*   `models/user_system.py`: Classe `UserSystem` para gerenciar a lista de usuários.
*   `test_auth.py`: Arquivo contendo os testes de unidade para as classes `User` e `UserSystem`.

## Passo a Passo para Execução dos Testes

Para rodar os testes de unidade e verificar o comportamento do sistema, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3** e o gerenciador de pacotes **pip** instalados em seu sistema.

### 2. Instalação do Pytest

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

1.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    # venv\Scripts\activate  
    ```

2.  **Instale o `pytest`:**
    ```bash
    pip install pytest
    ```

### 3. Execução dos Testes

Com o ambiente virtual ativado e o `pytest` instalado, navegue até o diretório raiz do projeto (`Autenticação`) e execute o comando:

```bash
pytest
```

### 4. Saída Esperada

O `pytest` irá executar todos os testes definidos em `test_auth.py`. Você deve ver uma saída indicando que todos os testes passaram.

**Observação Importante:** O teste `test_user_system_registrar_user_email_duplicado_falha_logica` **passa**, mas ele foi escrito especificamente para **demonstrar a falha de lógica (F2)** identificada no Relatório de V&V, onde o sistema **permite** o cadastro de e-mails duplicados. Em um sistema corrigido, este teste deveria ser ajustado para esperar uma exceção (`pytest.raises(ValueError)`).

## 5. Execução da Interface (Opcional)

Para rodar a interface de linha de comando do sistema:

```bash
python3 main.py
```

Isso iniciará o menu interativo para cadastrar e buscar usuários. Lembre-se que os dados são perdidos ao encerrar o programa.
