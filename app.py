from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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

        novo_cliente = Cliente(nome=nome, telefone=telefone, email=email)

        db.session.add(novo_cliente)
        db.session.commit()
        
        return "Ciente cadastrado com sucesso!"
    
    return render_template('cadastro.html')


# PAG LISTAS DE CLIENTES

@app.route('/clientes')
def listar_clientes():
    '''
    Docstring for listar_clientes
    '''
    lista = Cliente.query.all()

    return render_template('clientes.html', clientes=lista)


#============BANCO DE DADOS============
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oficina.db'

db = SQLAlchemy(app)


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)







    