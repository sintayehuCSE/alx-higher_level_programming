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
                           pool_pre_ping=True, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(State).filter(State.name.like('{}'
                                                      .format(argv[4]))).one_or_none()
    if qry:
        #for row in qry:
            print(qry.id)
    else:
        print('Not found')
    session.close()
