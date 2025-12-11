# Gestão de Clientes em Flask

Sistema de gerenciamento de clientes desenvolvido em Flask com MySQL. Permite listar, adicionar, visualizar, editar e deletar clientes, com os dados armazenados de forma persistente no MySQL.

# Características #

- ✅ **Persistência de dados** com MySQL (não perde dados ao reiniciar)
- ✅ **Arquitetura SOLID** para código limpo e manutenível
- ✅ **Comentários em português (BR)** para facilitar aprendizado
- ✅ **Repository Pattern** para abstração do banco de dados
- ✅ **Interface bem definida** permitindo trocar implementações facilmente

# Funcionalidades #

- **Listar Clientes**: Exibe a lista de todos os clientes cadastrados
- **Adicionar Cliente**: Permite cadastrar um novo cliente através de um formulário
- **Visualizar Dados do Cliente**: Exibe os detalhes de um cliente específico através do seu ID
- **Editar Cliente**: Permite modificar os dados de um cliente existente através de um formulário
- **Deletar Cliente**: Remove um cliente do sistema através do seu ID

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

# Próximos Passos e Melhorias #

Este projeto pode ser expandido com diversas melhorias, como:

- ✅ **Persistência de Dados**: ✅ **CONCLUÍDO** - Integrado MySQL para armazenar os dados de forma persistente
- **Validação de Dados**: Implementar validação nos formulários para garantir que os dados inseridos sejam válidos
- **Tratamento de Erros**: Adicionar tratamento de erros mais robusto para lidar com situações inesperadas
- **Interface de Usuário**: Melhorar a interface de usuário com CSS e JavaScript para uma experiência mais agradável
- **Segurança**: Implementar medidas de segurança, como proteção contra CSRF
- **Testes**: Adicionar testes unitários e de integração para garantir a qualidade do código
- **Autenticação e Autorização**: Implementar um sistema de login e controle de acesso

---

**Hugo Gonçalves**  
Sinta-se à vontade para contribuir e expandir este projeto. Sou um aluno em constante evolução para ajudar nesse mundo nosso!
