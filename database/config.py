"""
Configuração do banco de dados MySQL
Responsabilidade única: gerenciar configurações de conexão
"""
import os
from typing import Dict

class DatabaseConfig:
    """
    Classe de configuração do banco de dados
    Segue o princípio Single Responsibility (SOLID)
    """
    
    # Configurações padrão do MySQL
    # Você pode alterar essas variáveis ou usar variáveis de ambiente
    HOST: str = os.getenv('DB_HOST', 'localhost')
    PORT: int = int(os.getenv('DB_PORT', '3306'))
    USER: str = os.getenv('DB_USER', 'root')
    PASSWORD: str = os.getenv('DB_PASSWORD', '')
    DATABASE: str = os.getenv('DB_NAME', 'gerenciar_usuarios')
    CHARSET: str = 'utf8mb4'
    
    @classmethod
    def get_connection_string(cls) -> Dict[str, any]:
        """
        Retorna um dicionário com as configurações de conexão
        Útil para passar diretamente para o mysql.connector
        """
        return {
            'host': cls.HOST,
            'port': cls.PORT,
            'user': cls.USER,
            'password': cls.PASSWORD,
            'database': cls.DATABASE,
            'charset': cls.CHARSET,
            'autocommit': False  # Controlamos commits manualmente
        }
    
    @classmethod
    def get_connection_string_without_db(cls) -> Dict[str, any]:
        """
        Retorna configurações sem especificar o banco
        Útil para criar o banco de dados inicialmente
        """
        config = cls.get_connection_string()
        config.pop('database')
        return config

