"""
The function to create the database and the connection
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


def creae_db_session(host_name , db_name , user_name = None , password = None):
    """
    The function to create the database and the connection
    """


    # Create the connection string
    if user_name and password:
        connection_string = f'postgresql://{user_name}:{password}@{host_name}/{db_name}'
    else:
        connection_string = f'postgresql://{host_name}/{db_name}'

    # Create the engine
    engine = create_engine(connection_string)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    return engine, session







