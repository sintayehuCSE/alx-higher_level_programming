#!/usr/bin/python3
"""
A script that fetch one state from a DB using SQLAlchemy
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in q:
        print(row.id, row.name, sep=': ')
    session.close()
