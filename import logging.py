import logging
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models import User  # Ensure this is imported correctly
from bcrypt import hashpw, gensalt, checkpw

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class DbHelper:
    """
    A helper class for CRUD operations on the 'users' table.
    """

    def __init__(self, session: Session):
        self.session = session

    def hash_password(self, password: str) -> str:
        """Hashes the password securely using bcrypt."""
        return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Verifies a password against the stored hash."""
        return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    def create_user(self, username: str, password: str, userhash: str):
        """Creates a new user if they do not already exist."""
        try:
            existing_user = self.session.query(User).filter(User.username == username).first()
            if existing_user:
                logging.warning("User %s already exists.", username)
                return False

            hashed_password = self.hash_password(password)
            new_user = User(username=username, password=hashed_password, userhash=userhash)
            self.session.add(new_user)
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
