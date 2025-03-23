


from  pgsql_helper_kit import create_db_session, Db_Helper






test_engine , test_session = create_db_session(host_name= 'localhost' , db_name='test_db' , user_name='abhi', password='mysecretpassword')

print(test_engine)

print(test_session)

print(test_engine.url)

db_helper = Db_Helper(session=test_session, engine=test_engine)