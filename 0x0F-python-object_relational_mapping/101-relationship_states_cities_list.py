#!/usr/bin/python3
"""
List State object and their cities using configured relationship
"""
if __name__ == '__main__':
    from relationship_state import State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(State).join(City).order_by(State.id, City.id).all()
    for state in qry:
        print(state.id, state.name, sep=': ')
        for city in state.cities:
            print('    ', end='')
            print(city.id, city.name, sep=': ')

    session.close()
