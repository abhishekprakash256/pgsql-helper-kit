"""
The crud operations file for the pgsql_helper_kit package.
"""


from create_db import creae_db_session


test_engine , test_session = creae_db_session(host_name= 'localhost' , db_name='test_db' ,  password='mysecretpassword')
print(test_engine)
print(test_session)