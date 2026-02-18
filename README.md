# 🛠️ ZapBombas - Sistema de Gestão de Oficina

Este é um sistema de gestão para oficina mecânica desenvolvido com **Python** e o framework **Flask**. O objetivo do projeto é facilitar o cadastro de clientes e o controle de serviços realizados.

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **Flask**: Micro-framework web.
* **Flask-SQLAlchemy**: Extensão para manipulação do banco de dados SQL.
* **SQLite**: Banco de dados relacional leve (armazenado em arquivo local).

## 📂 Estrutura do Projeto

* `app.py`: Arquivo principal contendo as rotas e a lógica do servidor.
* `instance/`: Pasta que contém o arquivo do banco de dados (`oficina.db`).
* `templates/`: Pasta com os arquivos HTML do sistema.
    * `cadastro.html`: Formulário de entrada de dados.
    * `clientes.html`: Lista de clientes cadastrados.
* `venv/`: Ambiente virtual do Python.

## ⚙️ Funcionalidades Atuais

1.  **Banco de Dados**: Criação automática das tabelas `Cliente` (nome, email, telefone) e `Servico` (descrição, preço).
2.  **Cadastro de Clientes**: Rota `/cadastro` que recebe dados via formulário e salva no banco.
3.  **Listagem de Clientes**: Rota `/clientes` que busca as informações no banco e as exibe em uma lista dinámica.

## 🔧 Como rodar o projeto

1.  Ative o ambiente virtual:
    ```bash
    source venv/bin/activate  # No Linux/Mac
    # ou
    venv\Scripts\activate     # No Windows
    ```
2.  Instale as dependências:
    ```bash
    pip install flask flask-sqlalchemy
    ```
3.  Execute a aplicação:
    ```bash
    python app.py
    ```
4.  Acesse no navegador: `http://127.0.0.1:5000`

---
*Desenvolvido por Éveli durante os estudos de Python e Flask.*