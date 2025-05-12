# GestaoCliente-em-FLASK 

Este é um projeto simples de gestão de clientes desenvolvido utilizando o framework Flask (Python). Ele permite listar, adicionar, visualizar, editar e deletar clientes, com os dados armazenados temporariamente em memória.

->> Funcionalidades

Listar Clientes: Exibe a lista de todos os clientes cadastrados.
Adicionar Cliente: Permite cadastrar um novo cliente através de um formulário.
Visualizar Dados do Cliente: Exibe os detalhes de um cliente específico através do seu ID.
Editar Cliente: Permite modificar os dados de um cliente existente através de um formulário.
Deletar Cliente: Remove um cliente do sistema através do seu ID.

->> Estrutura do Projeto

O projeto é estruturado da seguinte forma:

* `cliente_route.py`: Define as rotas (URLs) e as funções de visualização (view functions) responsáveis pela lógica de cada funcionalidade relacionada aos clientes. Utiliza um Blueprint para modularizar as rotas.
* `database/cliente_db.py`: Simula um banco de dados em memória, armazenando os dados dos clientes na lista `CLIENTES`.
* `templates/`: Contém os arquivos HTML utilizados para renderizar as páginas da aplicação.
* `lista_cliente.html`: Template para exibir a lista de clientes.
* `form_criar_cliente.html`: Template para o formulário de criação e edição de clientes.
* `dados_do_cliente.html`: Template para exibir os detalhes de um cliente específico.
* `item_cliente.html`: Template para exibir um único item de cliente (usado após adicionar ou editar).

->> Próximos Passos e Melhorias ##

Este projeto é uma base simples e pode ser expandido com diversas melhorias, como:

Persistência de Dados: Integrar um banco de dados real em MySQL para armazenar os dados dos clientes de forma persistente. 
Validação de Dados: Implementar validação nos formulários para garantir que os dados inseridos pelos usuários sejam válidos.
Tratamento de Erros: Adicionar tratamento de erros mais robusto para lidar com situações inesperadas.
Interface de Usuário: Melhorar a interface de usuário com CSS e JavaScript para uma experiência mais agradável.
Segurança: Implementar medidas de segurança, como proteção contra CSRF.
Testes: Adicionar testes unitários e de integração para garantir a qualidade do código.
Autenticação e Autorização: Implementar um sistema de login e controle de acesso.

Hugo Gonçalves
Sinta-se à vontade para contribuir e expandir este meu projeto sou um aluno em constante evolução para ajuda nesse mundo nosso!

CRUD NA MEMORIA
![image](https://github.com/user-attachments/assets/e5ed96b1-d13b-4fb7-beb6-059f1d06cad4)


![image](https://github.com/user-attachments/assets/7a9b4cb6-6b0e-4dee-a2c1-6d8e10732206)


![image](https://github.com/user-attachments/assets/d16d6204-6431-411a-a4a8-d78690477abb)





