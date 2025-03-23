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

        print("Connected to:", self.engine.url)
        try:
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


    def check_user_exists(self, username: str) -> bool:
        """Checks if a user exists in the database."""

        return self.session.query(User).filter(User.username == username).first() is not None


    def get_user_password(self, username: str):
        """Retrieves the hashed password of a user."""

        user = self.session.query(User).filter(User.username == username).first()
        return user.password if user else None


    def update_user_password(self, username: str, new_password: str):
        """Updates the password of a user after hashing it."""

        try:
            user = self.session.query(User).filter(User.username == username).first()
            if not user:
                logging.warning("User %s not found.", username)
                return False

            user.password = self.hash_password(new_password)
            self.session.commit()
            logging.info("Password updated for user %s.", username)
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            logging.error("Error updating password: %s", str(e))
            return False


    def delete_user(self, username: str):
        """Deletes a user from the database."""

        try:
            user = self.session.query(User).filter(User.username == username).first()
            if not user:
                logging.warning("User %s not found.", username)
                return False

            self.session.delete(user)
            self.session.commit()
            logging.info("User %s deleted successfully.", username)
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            logging.error("Error deleting user: %s", str(e))
            return False


    def get_all_users(self):
        """Returns a list of all users."""

        return self.session.query(User).all()


    def get_user_hash(self, username: str):
        """Retrieves the user hash of a user."""
        
        user = self.session.query(User).filter(User.username == username).first()
        return user.userhash if user else None







db_helper = Db_Helper(session=test_session, engine=test_engine)


user = User(username='test_user4', password='test_password', userhash='test_hash')

print(db_helper.create_user(username='test_user5', password='parrot@984ks', userhash='89JBJFs'))
print(db_helper.get_user_password(username='test_user4'))
print(db_helper.get_user_hash(username='test_user4'))
print(db_helper.check_user_exists(username='test_user4'))
print(db_helper.get_all_users())
print(db_helper.update_user_password(username='test_user', new_password='new_password'))
print(db_helper.delete_user(username='test_user4'))
print(db_helper.get_all_users())
print(db_helper.check_user_exists(username='test_user4'))


def verify_password(input_password, stored_hashed_password):
    return checkpw(input_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))

if verify_password('parrot@984ks', db_helper.get_user_password('test_user5')):
    print("Password verified")
else:
    print("Password not verified")