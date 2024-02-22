#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
using sqlAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Creating all tables defined in the Base class
    Base.metadata.create_all(engine)

    # Creating a session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Creating a session object
    session = Session()

    # Querying all State objects from the database, ordered by id
    for instance in session.query(State).order_by(State.id):
        # Printing the id and name attributes of each State object
        print(instance.id, instance.name)
