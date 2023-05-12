from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

connection_string = "mysql+mysqlconnector://root:@localhost/impressoras"
engine_db = create_engine(connection_string)

Base = declarative_base()


class ApoioMulti(Base):
    __tablename__ = 'apoio_multi'

    idapoio_multi = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Biblioteca(Base):
    __tablename__ = 'biblioteca'

    idbiblioteca = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Clinica(Base):
    __tablename__ = 'clinica'

    idclinica = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Comercial(Base):
    __tablename__ = 'comercial'

    idcomercial = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Cordenacao(Base):
    __tablename__ = 'cordenacao'

    idcordenacao = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Psicologia(Base):
    __tablename__ = 'psicologia'

    idpsicologia = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class SecAcad(Base):
    __tablename__ = 'sec_acad'

    idsec_acad = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


class Secretaria(Base):
    __tablename__ = 'secretaria'

    idsecretaria = Column(Integer, primary_key=True)
    data = Column(String)
    contador = Column(Integer)


Session = sessionmaker(bind=engine_db)
session = Session()
