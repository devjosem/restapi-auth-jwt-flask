from extensions import db
from datetime import datetime

class User(db.Model):

    __tablename__ = "users"

    id  = db.Column(db.Integer , primary_key = True)
    nome = db.Column(db.String(50) , nullable = False)
    email = db.Column(db.String(80) , unique = True , nullable = False)
    is_admin = db.Column(db.Boolean ,  default = False)
    estado = db.Column(db.Boolean , default = True)
    date_created = db.Column(db.DateTime , default = datetime.utcnow)


    def __repr__(self):
        return f'<{self.nome}'