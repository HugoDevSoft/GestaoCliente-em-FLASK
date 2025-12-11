"""
Script para inicializar o banco de dados MySQL
Cria o banco e a tabela automaticamente
Execute este script uma vez antes de rodar a aplicação
"""
import mysql.connector
from mysql.connector import Error
from database.config import DatabaseConfig

def criar_banco_e_tabela():
    """
    Cria o banco de dados e a tabela de clientes
    Segue o princípio Single Responsibility
    """
    # Configuração sem especificar o banco (para criar o banco)
    config = DatabaseConfig.get_connection_string_without_db()
    
    try:
        # Conecta sem especificar o banco
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        # Cria o banco de dados se não existir
        print(f"Criando banco de dados '{DatabaseConfig.DATABASE}'...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DatabaseConfig.DATABASE} "
                      f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print(f"Banco de dados '{DatabaseConfig.DATABASE}' criado com sucesso!")
        
        # Seleciona o banco
        cursor.execute(f"USE {DatabaseConfig.DATABASE}")
        
        # Cria a tabela de clientes
        print("Criando tabela 'clientes'...")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            INDEX idx_email (email)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        cursor.execute(create_table_query)
        print("Tabela 'clientes' criada com sucesso!")
        
        # Insere dados iniciais (opcional)
        print("Inserindo dados iniciais...")
        dados_iniciais = [
            ('Hugo', 'teste@teste.com'),
            ('Priscila', 'teste1@teste.com'),
            ('Marcia', 'teste2@teste.com'),
            ('Sergio', 'teste3@teste.com'),
            ('Nicolas', 'teste4@teste.com'),
            ('Laura', 'teste5@teste.com'),
            ('Cintia', 'teste6@teste.com')
        ]
        
        insert_query = """
        INSERT INTO clientes (nome, email) 
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE nome=VALUES(nome)
        """
        
        cursor.executemany(insert_query, dados_iniciais)
        connection.commit()
        print(f"{len(dados_iniciais)} registros inseridos/atualizados!")
        
        cursor.close()
        print("\n✅ Banco de dados inicializado com sucesso!")
        
    except Error as e:
        print(f"❌ Erro ao inicializar banco de dados: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexão com MySQL fechada.")

if __name__ == "__main__":
    print("=" * 50)
    print("Inicializando banco de dados MySQL")
    print("=" * 50)
    criar_banco_e_tabela()

