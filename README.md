# pgsql-helper-kit

The PostgreSQL Helper Kit is a Python-based utility designed to simplify database interactions using SQLAlchemy. It provides an intuitive interface for performing CRUD (Create, Read, Update, Delete) operations efficiently, ensuring best practices in database management.

## Features
- User management (Create, Read, Update, Delete)
- Secure password hashing with bcrypt
- PostgreSQL integration using SQLAlchemy
- Structured logging for debugging

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhishekprakash256/pgsql-helper-kit.git
   cd pgsql-helper-kit
   ```

2. Install dependencies:
   ```bash
   pip install git+https://github.com/abhishekprakash256/pgsql-helper-kit.git  
   
   pip install -r requirements.txt
   ```

3. Docker commands 
```
docker exec -it postgres-container psql -U abhi -d test_db


## To run the docker container

docker run -d --name postgres-container \
  -e POSTGRES_USER=abhi \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=test_db \
  -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/init.sql \
  -p 5432:5432 \
  postgres

```

4. Check the data in SQL commands

```
docker exec -it postgres-container psql -U abhi -d test_db   #connect to docker container 

\c test_db    #connect to the database 

SELECT * FROM users;   # ; is imp , to check all  the entry

SELECT * FROM public.users;   #to the check all the entry

```



## Usage

### Database Setup
Create a PostgreSQL database and update your connection details in `create_db_session`.

### Example Usage

```python
from pgsql_helper_kit import create_db_session, User, Db_Helper

# Create database session
engine, session = create_db_session(
    host_name='localhost',
    db_name='test_db',
    user_name='abhi',
    password='mysecretpassword'
)
db_helper = Db_Helper(session, engine)

# Create a new user
db_helper.create_user(username='test_user', password='secure_pass', userhash='user_hash')

# Fetch user details
print(db_helper.get_user_password(username='test_user'))
print(db_helper.get_user_hash(username='test_user'))
print(db_helper.check_user_exists(username='test_user'))

# Update password
db_helper.update_user_password(username='test_user', new_password='new_secure_pass')

# Delete user
db_helper.delete_user(username='test_user')
```

## API Methods

### `create_user(username, password, userhash)`
Creates a new user with a hashed password.

### `get_user_password(username)`
Retrieves the hashed password of a user.

### `get_user_hash(username)`
Fetches the user hash.

### `check_user_exists(username)`
Checks if a user exists in the database.

### `update_user_password(username, new_password)`
Updates the password for a given user.

### `delete_user(username)`
Deletes a user from the database.

### `get_all_users()`
Retrieves all users from the database.

## Logging
Logging is enabled for debugging. Modify logging levels in `logging.basicConfig()`.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch and open a pull request.


