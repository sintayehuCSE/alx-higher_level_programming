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
    qry = session.query(City).order_by(City.id).all()
    for city in qry:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    session.close()
