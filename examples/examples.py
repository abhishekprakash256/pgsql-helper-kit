"""
The examples file for the pgsql_helper_kit package.
"""

from pgsql_helper_kit import create_db_session, User, Db_Helper

# Create the database session
engine, session = create_db_session(host_name='localhost', db_name='test_db', user_name='abhi', password= 'mysecretpassword')

# Create the Db_Helper object
db_helper = Db_Helper(session, engine)  # Create the Db_Helper object

# Create a new user 
print(db_helper.create_user(username='test_user5', password='parrot@984ks', userhash='89JBJFs'))
print(db_helper.get_user_password(username='test_user4'))
print(db_helper.get_user_hash(username='test_user4'))
print(db_helper.check_user_exists(username='test_user4'))
print(db_helper.get_all_users())
print(db_helper.update_user_password(username='test_user', new_password='new_password'))
print(db_helper.delete_user(username='test_user4'))
print(db_helper.get_all_users())
print(db_helper.check_user_exists(username='test_user4'))


