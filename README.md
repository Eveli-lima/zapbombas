# 🛠️ ZapBombas - Sistema de Gestão de Oficina

O **ZapBombas** é um sistema web desenvolvido para gerenciar a entrada e saída de equipamentos em uma oficina de manutenção (focado em bombas d'água e piscinas). O projeto permite o cadastro de clientes, abertura de Ordens de Serviço (O.S.) com fotos e acompanhamento de status.

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **Flask**: Framework web principal.
* **Flask-SQLAlchemy**: ORM para banco de dados.
* **SQLite**: Banco de dados local.
* **Bootstrap 5**: Framework CSS para interface responsiva e componentes (Modais, Cards, Accordions).
* **Jinja2**: Motor de templates para renderização HTML dinâmica.

## ⚙️ Funcionalidades Principais

### 1. Gestão de Clientes
* **Cadastro Completo**: Nome, Telefone e E-mail.
* **Listagem Inteligente**: Visualização em formato de "Acordeão" (lista expansível) para economizar espaço.
* **Link para WhatsApp**: Botão direto para iniciar conversa com o cliente.

### 2. Ordens de Serviço (O.S.)
* **Fluxo de Entrada (Check-in)**: Registro do equipamento assim que ele chega na oficina.
    * Dados: Equipamento, Marca/Modelo, Defeito Relatado.
    * **Upload de Fotos**: Capacidade de anexar foto do estado do equipamento na chegada.
* **Status da O.S.**: Acompanhamento visual (ex: "Em Análise").
* **Histórico**: Cada cliente possui uma página de perfil exclusiva listando todas as manutenções já realizadas.

### 3. Interface (UI/UX)
* **Layout Responsivo**: Funciona bem em computadores e celulares.
* **Modais**: Formulários de cadastro abrem sobre a tela sem precisar recarregar a página.
* **Feedback Visual**: Cores para status e formatação de valores monetários.

## 📂 Estrutura do Projeto

```text
zapbombas/
├── app.py                # Lógica principal, rotas e configuração de upload
├── models.py             # Modelos do Banco de Dados (Cliente e OrdemServico)
├── oficina.db            # Arquivo do banco de dados SQLite
├── static/
│   ├── style.css         # Estilos personalizados
│   └── uploads/          # Pasta onde as fotos dos equipamentos são salvas
├── templates/
│   ├── base.html         # Layout base (Menu e Rodapé) herdado pelas outras páginas
│   ├── cadastro.html     # Formulário de novos clientes
│   ├── clientes.html     # Lista de clientes (Accordion)
│   └── detalhe_cliente.html # Perfil do cliente + Histórico + Modal de Nova O.S.
└── venv/                 # Ambiente virtual
```

---

## 🔧 Como rodar o projeto

1.  **Clone ou baixe o repositório.**

2.  **Ative o ambiente virtual:**
    * **Linux/Mac:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install flask flask-sqlalchemy
    ```

4.  **Prepare o ambiente:**
    Certifique-se de que a pasta de uploads existe (ou crie manualmente):
    ```bash
    mkdir -p static/uploads
    ```

5.  **Execute a aplicação:**
    *(Na primeira execução, o banco `oficina.db` será criado automaticamente)*
    ```bash
    python app.py
    ```

6.  **Acesse no navegador:**
    [http://127.0.0.1:5000](http://127.0.0.1:5000)


*Desenvolvido por Éveli durante os estudos de Python e Flask.*