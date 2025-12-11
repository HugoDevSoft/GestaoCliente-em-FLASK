"""
Modelos de dados da aplicação
Define a estrutura dos dados que serão persistidos
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    """
    Modelo de dados para Cliente
    Representa um cliente no sistema
    """
    id: Optional[int]  # None quando é um novo cliente (ainda não tem ID no banco)
    nome: str
    email: str
    
    def to_dict(self) -> dict:
        """
        Converte o objeto Cliente para dicionário
        Útil para serialização JSON
        """
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Cliente':
        """
        Cria um objeto Cliente a partir de um dicionário
        Útil para deserialização
        """
        return cls(
            id=data.get('id'),
            nome=data.get('nome', ''),
            email=data.get('email', '')
        )

