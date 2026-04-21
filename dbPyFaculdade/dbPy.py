from sqlalchemy import create_engine, column, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("sqlite:///:memory:", echo=True)

base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column(Integer,primary_key = True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Usuario(id = {self.id}, nome = {self.nome}, idade {self.idade}"

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

usuario1 = Usuario(nome="Nicollas", idade= 19)
usuario2 = Usuario(nome = "Leticia", idade= 39)
session.add(usuario1)
session.add(usuario2)

session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)
