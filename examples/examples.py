"""
The examples file for the pgsql_helper_kit package.
"""

import logging
from pgsql_helper_kit import create_db_session, User, Db_Helper

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    try:
        # Create the database session
        engine, session = create_db_session(
            host_name='localhost',
            db_name='test_db',
            user_name='abhi',
            password='mysecretpassword'
        )
        db_helper = Db_Helper(session, engine)

        logging.info("Database session established successfully.")

        # Create a new user
        username = "test_user5"
        password = "parrot@984ks"
        userhash = "89JBJFs"

        logging.info(f"Creating user: {username}")
        user_created = db_helper.create_user(username, password, userhash)
        logging.info(f"User creation successful: {user_created}")

        # Fetch and display user details
        check_username = "test_user4"
        logging.info(f"\n Checking details for user: {check_username}")

        user_password = db_helper.get_user_password(username=check_username)
        logging.info(f"Retrieved password: {user_password}")

        user_hash = db_helper.get_user_hash(username=check_username)
        logging.info(f"Retrieved user hash: {user_hash}")

        user_exists = db_helper.check_user_exists(username=check_username)
        logging.info(f"User exists: {user_exists}")

        # Retrieve all users
        logging.info("\n Fetching all users in the database:")
        users = db_helper.get_all_users()
        logging.info(f"All users: {users}")

        # Update user password
        logging.info("\n Updating user password")
        update_result = db_helper.update_user_password(username="test_user", new_password="new_password")
        logging.info(f"Password update successful: {update_result}")

        # Delete user
        logging.info("\n Deleting user")
        delete_result = db_helper.delete_user(username=check_username)
        logging.info(f"User deletion successful: {delete_result}")

        # Check users again after deletion
        logging.info("\n Fetching users after deletion:")
        users_after_deletion = db_helper.get_all_users()
        logging.info(f"All users after deletion: {users_after_deletion}")

        user_exists_after_deletion = db_helper.check_user_exists(username=check_username)
        logging.info(f"User exists after deletion: {user_exists_after_deletion}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
