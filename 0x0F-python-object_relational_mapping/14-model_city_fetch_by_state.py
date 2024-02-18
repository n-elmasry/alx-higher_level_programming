#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id).first().name
        print(f'{state_name}: ({city.id}) {city.name}')

    session.close()
