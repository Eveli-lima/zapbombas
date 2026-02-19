from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER ='static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#============BANCO DE DADOS============
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oficina.db'

from models import db, Cliente, OrdemServico
db.init_app(app)
with app.app_context():
    db.create_all()

#================ROTAS=================

# PAG INICIAL
@app.route('/') 
def home():
    """
    Docstring for home
    """
    return "Página Inicial ZAP BOMBAS"

 # PAG CADASTRO DE CLIENTES
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar_cliente():
    """
    Docstring for cadastrar_cliente
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']

        #print(f"DADOS RECEBIDOS: Nome:={nome}, Telefone:={telefone}, Email:={email}")

        novo_cliente = Cliente(nome=nome, telefone=telefone, email=email)

        db.session.add(novo_cliente)
        db.session.commit()
        
        return redirect(url_for('listar_clientes'))
    
    return render_template('cadastro.html')


# PAG LISTAS DE CLIENTES

@app.route('/clientes')
def listar_clientes():
    '''
    Docstring for listar_clientes
    '''
    lista = Cliente.query.all()

    return render_template('clientes.html', clientes=lista)

# PAG DO CLIENTE

@app.route('/cliente/<int:id>')

def detalhe_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    historico = OrdemServico.query.filter_by(cliente_id=id).all()

    return render_template('detalhe_cliente.html', cliente=cliente, servicos=historico)

# ROTA PARA NOVA ORDEM DE SERVIÇO

@app.route('/nova_os/<int:cliente_id>', methods=['POST'])
def adicionar_os(cliente_id):
    # Pega os dados do formulário
    equipamento = request.form['equipamento']
    marca = request.form['marca']
    defeito = request.form['defeito_relatado']
    data = request.form['data_entrada']
    
    # Lógica para salvar a FOTO
    foto = request.files['foto'] # Pega o arquivo do input
    nome_foto = None
    
    if foto:
        filename = secure_filename(foto.filename) # Limpa o nome do arquivo para segurança
        # Salva na pasta static/uploads
        foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        nome_foto = filename

    # Cria a O.S. com status "Em Análise"
    nova_os = OrdemServico(
        equipamento=equipamento,
        marca=marca,
        defeito_relatado=defeito,
        data_entrada=data,
        foto_caminho=nome_foto,
        cliente_id=cliente_id,
        status='Em Análise' # Começa assim
    )
    
    db.session.add(nova_os)
    db.session.commit()
    
    return redirect(url_for('detalhe_cliente', id=cliente_id))

if __name__ == '__main__':
    app.run(debug=True)