
"""
The file to test the connections
"""

import pytest
from pgsql_helper_kit import create_db_session, Db_Helper
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import logging
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select



Base = declarative_base()

def test_create_db_session():
    """
    The function to test the create_db_session function
    """
    engine, session = create_db_session(host_name='localhost', db_name='test_db', user_name='abhi', password
    ='mysecretpassword')
    assert engine
    assert session
    assert engine.url
    assert engine.url.database == 'test_db'
    assert engine.url.host == 'localhost'
    assert engine.url.username == 'abhi'
    assert engine.url.password == 'mysecretpassword'
    assert engine.url.port == 5432
    assert engine.url.drivername == 'postgresql'
    
