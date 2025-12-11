-- Script SQL para criar o banco de dados e a tabela de clientes
-- Execute este script no MySQL antes de rodar a aplicação

-- Cria o banco de dados (se não existir)
CREATE DATABASE IF NOT EXISTS gerenciar_usuarios 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Seleciona o banco de dados
USE gerenciar_usuarios;

-- Cria a tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insere alguns dados iniciais (opcional)
INSERT INTO clientes (nome, email) VALUES
('Hugo', 'teste@teste.com'),
('Priscila', 'teste1@teste.com'),
('Marcia', 'teste2@teste.com'),
('Sergio', 'teste3@teste.com'),
('Nicolas', 'teste4@teste.com'),
('Laura', 'teste5@teste.com'),
('Cintia', 'teste6@teste.com')
ON DUPLICATE KEY UPDATE nome=VALUES(nome);

