from flask import Flask, url_for, render_template

# o import do url_for serve pra montar URL interna do nosso servidor web de acordo com a função da rota que voce quer 
# o import do render_template serve tanto para busca na pasta templates um arquivos HTML quanto manda variavéis do back-end para o front-end através das **
# **variáveis de contexto {% %} e outras

# A inicialização precisa está sempre no Top do código
app = Flask(__name__)

# rotas
@app.route("/")
# a função que recebe a requesição sempre precisa reporta alguma coisa um HTML, String ou um Json mas voce deve retorna algo
def ola_mundo():
    ltitulo = "Gestão de Usuarios"
    listausuarios = [
        {"nome": "Hugo", "membro_ativo": True},
        {"nome": "Priscila", "membro_ativo": False},
        {"nome": "Samuel", "membro_ativo": True},
    ]
    
    return render_template('index.html', htmltitulo=ltitulo, htmlusuarios=listausuarios)

     
@app.route("/teste")
def ola_mundoteste():
    
    # usando url_for colocando f antes da função e porque usar isso | facil manutenção, evita erro de digitação, gera url dinâmicas e mais segurança.
    return f"<a href='{ url_for ('pag_aula2_youtube') }'>Pagína do link da Aulas</a>" 


@app.route("/aulasFlask2")
# a função que recebe a requesição sempre precisa reporta alguma coisa um HTML, String ou um Json mas voce deve retorna algo
def pag_aula2_youtube():
    return """
    <b>Videos de Dev Web com Flask e Python Aula2
    <a href="https://www.youtube.com/watch?v=fkXlSyWiXVg">Link do Youtube</a>
    """
    
@app.route("/aulasFlask3")
# a função que recebe a requesição sempre precisa reporta alguma coisa um HTML, String ou um Json mas voce deve retorna algo
def pag_aula3_youtube():
    return """
    <b>Videos de Dev Web com Flask e Python Aula3
    <a href="https://www.youtube.com/watch?v=TO2yRV-QO8U">Link do Youtube</a>
    """
    
# Execução
app.run(debug=True)