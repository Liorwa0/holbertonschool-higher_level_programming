#!/usr/bin/python3
"""
Prints the State object with the name passed as argument.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name():
    """
    Searches for state by name and prints its id.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == sys.argv[4]
    ).first()

    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()


if __name__ == "__main__":
    get_state_by_name()
