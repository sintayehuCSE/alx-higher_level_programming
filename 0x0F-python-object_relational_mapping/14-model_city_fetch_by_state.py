#!/usr/bin/python3
"""
Prints all city objects/instance in DB that match search criteria
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import State, Base
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    qry = session.query(State.name, City.id, City.nam
                        e).join(City).order_by(City.id).all()
    for stateName, cityId, cityName in qry:
        print('{}: ({}) {}'.format(stateName, cityId, cityName))
    session.close()
