# Gestão de Clientes em Flask

Sistema de gerenciamento de clientes desenvolvido em Flask com MySQL.

# Características #

- ✅ **Persistência de dados** com MySQL (não perde dados ao reiniciar)
- ✅ **Arquitetura SOLID** para código limpo e manutenível
- ✅ **Comentários em português (BR)** para facilitar aprendizado
- ✅ **Repository Pattern** para abstração do banco de dados
- ✅ **Interface bem definida** permitindo trocar implementações facilmente

# Pré-requisitos #

- Python 3.7+
- MySQL instalado e rodando
- pip

# Instalação #

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Configure o banco de dados:**
   - Edite `database/config.py` com suas credenciais MySQL
   - OU configure variáveis de ambiente (veja `SETUP_MYSQL.md`)

3. **Inicialize o banco:**
```bash
python database/init_db.py
```

4. **Execute a aplicação:**
```bash
python main.py
```

## 📚 Documentação

Consulte `SETUP_MYSQL.md` para instruções detalhadas de configuração.

# Arquitetura #

O projeto segue os princípios SOLID:

- **Single Responsibility**: Cada classe tem uma única responsabilidade
- **Open/Closed**: Extensível sem modificar código existente
- **Liskov Substitution**: Interfaces bem definidas
- **Interface Segregation**: Interfaces específicas
- **Dependency Inversion**: Depende de abstrações, não implementações

# Estrutura #

```
├── database/
│   ├── config.py              # Configurações MySQL
│   ├── models.py              # Modelos de dados
│   ├── repository.py          # Interface (SOLID)
│   ├── mysql_repository.py    # Implementação MySQL
│   ├── cliente_db.py          # Camada de acesso
│   └── init_db.py             # Inicialização do banco
├── routes/
│   └── cliente_route.py       # Rotas HTTP
└── main.py                    # Aplicação Flask
```
