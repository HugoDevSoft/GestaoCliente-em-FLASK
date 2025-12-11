"""
Rotas para gerenciamento de clientes
Agora usa MySQL através da camada de acesso aos dados
Segue o princípio Single Responsibility: apenas responsável por rotas HTTP
"""
from flask import Blueprint, render_template, request, abort
from database.cliente_db import (
    get_clientes, 
    get_cliente_por_id, 
    criar_cliente, 
    atualizar_cliente, 
    deletar_cliente
)

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')  
def lista_clientes():
    """
    Lista todos os clientes cadastrados
    Busca os dados do banco MySQL
    """
    clientes = get_clientes()
    return render_template('lista_cliente.html', clientes=clientes)


@cliente_route.route('/', methods=['POST']) 
def add_cliente():
    """
    Cria um novo cliente no banco de dados MySQL
    Recebe os dados via JSON e persiste no banco
    """
    data = request.json
    
    # Validação básica dos dados
    if not data or 'nome' not in data or 'email' not in data:
        return {'error': 'Nome e email são obrigatórios'}, 400
    
    # Cria o cliente usando a função do repositório
    novo_cliente = criar_cliente(
        nome=data['nome'],
        email=data['email']
    )
    
    return render_template('item_cliente.html', cliente=novo_cliente)
       

@cliente_route.route('/new') 
def form_criar_cliente():
    """
    Renderiza o formulário para cadastrar um novo cliente
    """
    return render_template('form_criar_cliente.html')
   

@cliente_route.route('/<int:cliente_id>')  
def dados_do_cliente(cliente_id):
    """
    Busca e exibe os dados de um cliente específico pelo ID
    Retorna 404 se o cliente não for encontrado
    """
    cliente = get_cliente_por_id(cliente_id)
    
    if cliente is None:
        abort(404, description="Cliente não encontrado")
    
    return render_template('dados_do_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')  
def form_editar_cliente(cliente_id):
    """
    Renderiza o formulário para editar um cliente existente
    Carrega os dados do cliente do banco MySQL
    """
    cliente = get_cliente_por_id(cliente_id)
    
    if cliente is None:
        abort(404, description="Cliente não encontrado")
    
    return render_template('form_criar_cliente.html', cliente=cliente)
    

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])  
def atualiza_cliente(cliente_id):
    """
    Atualiza os dados de um cliente existente no banco MySQL
    Recebe os dados via JSON e atualiza no banco
    """
    data = request.json
    
    # Validação básica dos dados
    if not data or 'nome' not in data or 'email' not in data:
        return {'error': 'Nome e email são obrigatórios'}, 400
    
    # Atualiza o cliente usando a função do repositório
    cliente_atualizado = atualizar_cliente(
        cliente_id=cliente_id,
        nome=data['nome'],
        email=data['email']
    )
    
    if cliente_atualizado is None:
        return {'error': 'Cliente não encontrado'}, 404
    
    return render_template('item_cliente.html', cliente=cliente_atualizado)
    

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])  
def deleta_cliente(cliente_id):
    """
    Deleta um cliente do banco MySQL pelo ID
    Retorna sucesso ou erro
    """
    sucesso = deletar_cliente(cliente_id)
    
    if sucesso:
        return {'delete': 'ok', 'message': 'Cliente deletado com sucesso'}
    else:
        return {'error': 'Cliente não encontrado'}, 404
