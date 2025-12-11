"""
Interface do repositório (Repository Pattern)
Segue o princípio Dependency Inversion do SOLID
Permite trocar a implementação sem alterar o código que usa o repositório
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from database.models import Cliente

class IClienteRepository(ABC):
    """
    Interface abstrata para o repositório de clientes
    Define o contrato que todas as implementações devem seguir
    """
    
    @abstractmethod
    def criar(self, cliente: Cliente) -> Cliente:
        """
        Cria um novo cliente no banco de dados
        Retorna o cliente criado com o ID gerado
        """
        pass
    
    @abstractmethod
    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        """
        Busca um cliente pelo ID
        Retorna None se não encontrar
        """
        pass
    
    @abstractmethod
    def buscar_todos(self) -> List[Cliente]:
        """
        Retorna todos os clientes cadastrados
        """
        pass
    
    @abstractmethod
    def atualizar(self, cliente: Cliente) -> Optional[Cliente]:
        """
        Atualiza os dados de um cliente existente
        Retorna o cliente atualizado ou None se não encontrar
        """
        pass
    
    @abstractmethod
    def deletar(self, cliente_id: int) -> bool:
        """
        Deleta um cliente pelo ID
        Retorna True se deletou, False se não encontrou
        """
        pass

