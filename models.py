from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)


class OrdemServico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ENTRADA
    data_entrada = db.Column(db.String(20), nullable=False)
    equipamento = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(50))
    defeito_relatado = db.Column(db.Text)
    foto_caminho = db.Column(db.String(200))

    status = db.Column(db.String(50), default='Em Análise')

    # ORÇAMENTO
    diagnostico_tecnico = db.Column(db.Text)
    pecas = db.Column(db.Text)
    mao_de_obra = db.Column(db.Float)
    valor_total = db.Column(db.Float)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
