from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dog
from testing.conftest import SQLITE_URL
engine = create_engine(SQLITE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()


def create_table(base, engine):
    if __name__ == "__main__":
        engine = create_engine(SQLITE_URL)
        base.metadata.create.all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()
    

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    session.query(Dog).update({Dog.breed : breed})
    session.commit()