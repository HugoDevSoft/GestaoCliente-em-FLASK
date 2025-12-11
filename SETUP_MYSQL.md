# Guia de Configuração MySQL

## 📋 Pré-requisitos

1. **MySQL instalado** no seu computador
2. **Python 3.7+** instalado
3. **pip** para instalar dependências

## 🚀 Passo a Passo

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Banco de Dados

Edite o arquivo `database/config.py` e ajuste as configurações do MySQL:

```python
HOST: str = 'localhost'      # Endereço do servidor MySQL
PORT: int = 3306             # Porta do MySQL (padrão: 3306)
USER: str = 'root'           # Seu usuário MySQL
PASSWORD: str = 'sua_senha'  # Sua senha MySQL
DATABASE: str = 'gerenciar_usuarios'  # Nome do banco de dados
```

**OU** configure usando variáveis de ambiente:

```bash
# Windows PowerShell
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_USER="root"
$env:DB_PASSWORD="sua_senha"
$env:DB_NAME="gerenciar_usuarios"

# Linux/Mac
export DB_HOST="localhost"
export DB_PORT="3306"
export DB_USER="root"
export DB_PASSWORD="sua_senha"
export DB_NAME="gerenciar_usuarios"
```

### 3. Inicializar o Banco de Dados

Execute o script de inicialização:

```bash
python database/init_db.py
```

Este script irá:
- ✅ Criar o banco de dados `gerenciar_usuarios`
- ✅ Criar a tabela `clientes`
- ✅ Inserir dados iniciais (os 7 clientes que você tinha em memória)

### 4. Executar a Aplicação

```bash
python main.py
```

A aplicação estará rodando em `http://localhost:5000`

## 📁 Estrutura do Projeto (Arquitetura SOLID)

```
GerenciarUsuarios/
├── database/
│   ├── config.py              # Configurações do MySQL
│   ├── models.py              # Modelos de dados (Cliente)
│   ├── repository.py          # Interface do repositório (SOLID)
│   ├── mysql_repository.py    # Implementação MySQL
│   ├── cliente_db.py          # Camada de acesso (compatibilidade)
│   ├── init_db.py             # Script de inicialização
│   └── schema.sql             # Script SQL manual
├── routes/
│   ├── cliente_route.py       # Rotas HTTP (atualizadas)
│   └── homer.py               # Rota home
├── templates/                 # Templates HTML
├── static/                    # CSS e JS
├── main.py                    # Aplicação Flask
└── requirements.txt           # Dependências Python
```

## 🏗️ Princípios SOLID Aplicados

### ✅ Single Responsibility Principle (SRP)
- Cada classe tem uma única responsabilidade:
  - `DatabaseConfig`: apenas configurações
  - `Cliente`: apenas modelo de dados
  - `MySQLClienteRepository`: apenas operações MySQL
  - Rotas: apenas lógica HTTP

### ✅ Open/Closed Principle (OCP)
- Você pode criar novas implementações de `IClienteRepository` sem modificar código existente
- Exemplo: poderia criar `PostgreSQLClienteRepository` sem alterar as rotas

### ✅ Liskov Substitution Principle (LSP)
- Qualquer implementação de `IClienteRepository` pode substituir outra
- O código que usa o repositório não precisa saber qual implementação está sendo usada

### ✅ Interface Segregation Principle (ISP)
- A interface `IClienteRepository` é específica e focada apenas em clientes
- Não força implementações desnecessárias

### ✅ Dependency Inversion Principle (DIP)
- As rotas dependem da abstração (`IClienteRepository`), não da implementação concreta
- Facilita testes e manutenção

## 🔧 Troubleshooting

### Erro: "Access denied for user"
- Verifique usuário e senha no `config.py`
- Certifique-se que o MySQL está rodando

### Erro: "Can't connect to MySQL server"
- Verifique se o MySQL está instalado e rodando
- Verifique o HOST e PORT no `config.py`

### Erro: "Unknown database"
- Execute o script `database/init_db.py` primeiro

## 📝 Notas Importantes

- Os dados agora são **persistentes** - não serão perdidos ao reiniciar a aplicação
- O banco de dados MySQL mantém os dados mesmo após desligar o computador
- Todos os comentários estão em **português (BR)** para facilitar o entendimento
- A arquitetura segue **SOLID** para facilitar manutenção e evolução do código

