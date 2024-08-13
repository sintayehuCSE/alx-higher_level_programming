#!/usr/bin/python3
"""
Creates state and its cities simultaneously
"""
if __name__ == '__main__':
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = State(name='California')
    city = City(name='San Francisco')
    obj.cities.append(city)
    session.add(obj)
    session.add(city)
    session.commit()
