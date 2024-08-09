#!/usr/bin/python3
"""
A script that list all available state from a DB using SQLAlchemy
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(State).order_by(State.id).all()
    for row in qry:
        print(row.id, row.name, sep=': ')
    session.close()
