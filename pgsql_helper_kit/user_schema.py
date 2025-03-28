"""
create user schema
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    userhash = Column(String, nullable=False)  # Store user hash

    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"

# Create the table (if it doesn't exist)
