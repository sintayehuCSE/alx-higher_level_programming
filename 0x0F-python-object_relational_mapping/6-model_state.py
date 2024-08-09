#!/usr/bin/python3
"""
Starts a linink of declarative class to table in database
"""
if __name__ == "__main__":
    from model_state import engine, Base
    Base.metadata.create_all(engine)
