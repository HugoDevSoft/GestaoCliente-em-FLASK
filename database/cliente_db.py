"""
Camada de acesso aos dados de clientes
Agora usa MySQL através do repositório seguindo SOLID
Segue o princípio Dependency Inversion: depende da abstração (interface)
"""
from database.mysql_repository import MySQLClienteRepository
from database.models import Cliente

# Instância única do repositório (Singleton pattern)
# Isso garante que todas as partes da aplicação usem a mesma conexão
_repository: MySQLClienteRepository = None

def get_repository() -> MySQLClienteRepository:
    """
    Retorna a instância do repositório (Singleton)
    Cria uma nova instância apenas na primeira chamada
    """
    global _repository
    if _repository is None:
        _repository = MySQLClienteRepository()
    return _repository

# Funções de compatibilidade com o código antigo
# Permitem migração gradual sem quebrar o código existente
def get_clientes():
    """
    Retorna todos os clientes como lista de dicionários
    Mantém compatibilidade com código antigo
    """
    repository = get_repository()
    clientes = repository.buscar_todos()
    return [cliente.to_dict() for cliente in clientes]

def get_cliente_por_id(cliente_id: int):
    """
    Busca um cliente por ID e retorna como dicionário
    Mantém compatibilidade com código antigo
    """
    repository = get_repository()
    cliente = repository.buscar_por_id(cliente_id)
    return cliente.to_dict() if cliente else None

def criar_cliente(nome: str, email: str):
    """
    Cria um novo cliente e retorna como dicionário
    Mantém compatibilidade com código antigo
    """
    repository = get_repository()
    novo_cliente = Cliente(id=None, nome=nome, email=email)
    cliente_criado = repository.criar(novo_cliente)
    return cliente_criado.to_dict()

def atualizar_cliente(cliente_id: int, nome: str, email: str):
    """
    Atualiza um cliente existente e retorna como dicionário
    Mantém compatibilidade com código antigo
    """
    repository = get_repository()
    cliente = Cliente(id=cliente_id, nome=nome, email=email)
    cliente_atualizado = repository.atualizar(cliente)
    return cliente_atualizado.to_dict() if cliente_atualizado else None

def deletar_cliente(cliente_id: int):
    """
    Deleta um cliente pelo ID
    Retorna True se deletou, False caso contrário
    """
    repository = get_repository()
    return repository.deletar(cliente_id)

# Função para manter compatibilidade com código que usa CLIENTES diretamente
def CLIENTES():
    """
    Função que retorna os clientes do banco de dados
    Mantém compatibilidade com código antigo que usa CLIENTES como variável
    """
    return get_clientes()
