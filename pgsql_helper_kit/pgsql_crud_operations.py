"""
The crud operations file for the pgsql_helper_kit package.
"""


from create_db import create_db_session
from user_schema import User
import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from bcrypt import hashpw, gensalt, checkpw


#testing the function
test_engine , test_session = create_db_session(host_name= 'localhost' , db_name='test_db' , user_name='abhi', password='mysecretpassword')
print(test_engine)
print(test_session)

print(test_engine.url)






class Db_Helper():
    """
    The class to make the CRUD operations
    """

    def __init__(self,session, engine):
        self.session = session
        self.engine = engine

    def hash_password(self, password: str) -> str:
        """Hashes the password securely using bcrypt."""
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")
    
    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Verifies a password against the stored hash."""
        return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    def create_user(self, username: str, password: str, userhash: str):
        """Creates a new user if they do not already exist."""
        all_users = self.session.query(User).all()
        print("All users in SQLAlchemy:", all_users)

        print("Connected to:", self.engine.url)
        try:
            #all_users = self.session.query(User).all()
            #print("All users in SQLAlchemy:", all_users)

            existing_user = self.session.query(User).filter(User.username == username).first()
            #self.session.expire(existing_user)
            if existing_user:
                print("Before insert:", existing_user)
                logging.warning("User %s already exists.", username)
                return False

            hashed_password = self.hash_password(password)
            new_user = User(username=username, password=hashed_password, userhash=userhash)
            self.session.add(new_user)
            self.session.flush()
            self.session.commit()
            logging.info("User %s created successfully.", username)
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            logging.error("Error creating user: %s", str(e))
            return False




db_helper = Db_Helper(session=test_session, engine=test_engine)


user = User(username='test_user4', password='test_password', userhash='test_hash')



print(db_helper.create_user(user.username, user.password, user.userhash))


