from flask import Blueprint, render_template, request
from database.cliente_db import CLIENTES

cliente_route = Blueprint('cliente', __name__)


@cliente_route.route('/')  
def lista_clientes():
    """Listar todos cliente """
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/', methods= ['POST']) 
def add_cliente():
    """Inserir o novo cliente ao servidor/banco de dados"""
    data = request.json
    novo_usuario = { 
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }
    
    CLIENTES.append(novo_usuario)
    
    return render_template('item_cliente.html', cliente=novo_usuario)
       
@cliente_route.route('/new') 
def form_criar_cliente():
    """formulario para cadastrar novo cliente"""
    return render_template('form_criar_cliente.html')
   
@cliente_route.route('/<int:cliente_id>')  
def dados_do_cliente(cliente_id):
    """Obter os dados de um cliente específico através do id."""
    
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('dados_do_cliente.html', cliente=cliente)

#@cliente_route.route('/<int:cliente_id>')
#def dados_do_cliente(cliente_id):
    """Obter os dados de um cliente específico através do id."""
    
    cliente = next((c for c in CLIENTES if c['id'] == cliente_id), None)
    

    return render_template('dados_do_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/edit')  
def form_editar_cliente(cliente_id):
    """renderizar um formulario para editar um cliente já existente"""
    
    cliente = {}
   
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_criar_cliente.html', cliente=cliente)
    
@cliente_route.route('/<int:cliente_id>/uptade', methods=['PUT'])  
def atualiza_cliente(cliente_id):
    """atualiza os dados do cliente"""
    # obter dados do formulário de edição
    data = request.json
    
    cliente_editado = {}
    # obter usuario pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            
            cliente_editado = c
    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)
    
    
    

@cliente_route.route('/<int:cliente_id>/delete ', methods=['DELETE'])  
def deleta_cliente(cliente_id):
    """atualiza os dados do cliente"""
    global CLIENTES    
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {'delete': 'ok'}
    


   