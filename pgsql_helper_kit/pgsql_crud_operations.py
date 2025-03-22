"""
The crud operations file for the pgsql_helper_kit package.
"""


from create_db import creae_db_session
from user_schema import User



#testing the function
test_engine , test_session = creae_db_session(host_name= 'localhost' , db_name='test_db' ,  password='mysecretpassword')
print(test_engine)
print(test_session)


user = User(username='test_user', password='test_password', userhash='test_hash')

test_session.add(user)




class Db_Helper():
    """
    The class to make the CRUD operations
    """

    def __init__(self,session, engine):
        self.session = session
        self.engine = engine

    
    

