from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    email= db.Column(db.String(40), unique=True)
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username,password,name,email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Livro(db.Model):
    __tablename__= "livros"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    autor = db.Column(db.String(40))
    categoria = db.Column(db.String(50))
    idioma = db.Column(db.String(30))
    
    def __init__(self,nome,autor,categoria,idioma):
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        self.idioma = idioma

    def __repr__(self):
        return "<Livro %r>" % self.id

    
