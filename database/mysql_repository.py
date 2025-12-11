"""
Implementação do repositório usando MySQL
Segue os princípios SOLID:
- Single Responsibility: apenas responsável por operações MySQL
- Dependency Inversion: implementa a interface IClienteRepository
"""
import mysql.connector
from mysql.connector import Error
from typing import List, Optional
from database.repository import IClienteRepository
from database.models import Cliente
from database.config import DatabaseConfig

class MySQLClienteRepository(IClienteRepository):
    """
    Implementação concreta do repositório usando MySQL
    """
    
    def __init__(self):
        """Inicializa o repositório com as configurações do banco"""
        self.config = DatabaseConfig.get_connection_string()
    
    def _get_connection(self):
        """
        Cria e retorna uma conexão com o banco de dados
        Método privado para encapsular a lógica de conexão
        """
        try:
            connection = mysql.connector.connect(**self.config)
            return connection
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise
    
    def criar(self, cliente: Cliente) -> Cliente:
        """
        Insere um novo cliente no banco de dados
        Retorna o cliente com o ID gerado pelo banco
        """
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            # Query SQL para inserir novo cliente
            query = """
                INSERT INTO clientes (nome, email)
                VALUES (%s, %s)
            """
            values = (cliente.nome, cliente.email)
            
            cursor.execute(query, values)
            connection.commit()
            
            # Obtém o ID gerado pelo banco
            cliente_criado_id = cursor.lastrowid
            
            cursor.close()
            
            # Retorna o cliente com o ID gerado
            return Cliente(id=cliente_criado_id, nome=cliente.nome, email=cliente.email)
            
        except Error as e:
            if connection:
                connection.rollback()
            print(f"Erro ao criar cliente: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()
    
    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        """
        Busca um cliente pelo ID
        Retorna None se não encontrar
        """
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor(dictionary=True)  # Retorna como dicionário
            
            query = "SELECT id, nome, email FROM clientes WHERE id = %s"
            cursor.execute(query, (cliente_id,))
            
            resultado = cursor.fetchone()
            cursor.close()
            
            if resultado:
                return Cliente(
                    id=resultado['id'],
                    nome=resultado['nome'],
                    email=resultado['email']
                )
            return None
            
        except Error as e:
            print(f"Erro ao buscar cliente por ID: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()
    
    def buscar_todos(self) -> List[Cliente]:
        """
        Retorna todos os clientes cadastrados
        """
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = "SELECT id, nome, email FROM clientes ORDER BY id"
            cursor.execute(query)
            
            resultados = cursor.fetchall()
            cursor.close()
            
            # Converte os resultados em objetos Cliente
            clientes = []
            for resultado in resultados:
                clientes.append(Cliente(
                    id=resultado['id'],
                    nome=resultado['nome'],
                    email=resultado['email']
                ))
            
            return clientes
            
        except Error as e:
            print(f"Erro ao buscar todos os clientes: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()
    
    def atualizar(self, cliente: Cliente) -> Optional[Cliente]:
        """
        Atualiza os dados de um cliente existente
        Retorna o cliente atualizado ou None se não encontrar
        """
        if cliente.id is None:
            raise ValueError("ID do cliente é obrigatório para atualização")
        
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            query = """
                UPDATE clientes 
                SET nome = %s, email = %s
                WHERE id = %s
            """
            values = (cliente.nome, cliente.email, cliente.id)
            
            cursor.execute(query, values)
            connection.commit()
            
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            # Se atualizou alguma linha, retorna o cliente atualizado
            if linhas_afetadas > 0:
                return cliente
            return None
            
        except Error as e:
            if connection:
                connection.rollback()
            print(f"Erro ao atualizar cliente: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()
    
    def deletar(self, cliente_id: int) -> bool:
        """
        Deleta um cliente pelo ID
        Retorna True se deletou, False se não encontrou
        """
        connection = None
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM clientes WHERE id = %s"
            cursor.execute(query, (cliente_id,))
            
            connection.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            
            # Retorna True se deletou pelo menos uma linha
            return linhas_afetadas > 0
            
        except Error as e:
            if connection:
                connection.rollback()
            print(f"Erro ao deletar cliente: {e}")
            raise
        finally:
            if connection and connection.is_connected():
                connection.close()

