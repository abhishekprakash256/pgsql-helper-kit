
"""
The file to test the connections
"""

from unittest import TestCase
from unittest.mock import MagicMock
from pgsql_helper_kit import Db_Helper, User  # Import your DB helper and model

class TestDbHelper(TestCase):
    def setUp(self):
        """Setup mock session"""
        self.mock_session = MagicMock()
        self.mock_engine = MagicMock()
        self.db_helper = Db_Helper(self.mock_session, self.mock_engine)

    def test_create_user_success(self):
        """Test successful user creation"""
        self.mock_session.query().filter().first.return_value = None  # No existing user
        self.mock_session.add = MagicMock()
        self.mock_session.commit = MagicMock()

        result = self.db_helper.create_user("test_user", "secure_password", "hash123")

        self.assertTrue(result)
        self.mock_session.add.assert_called_once()  # Ensure the user was added
        self.mock_session.commit.assert_called_once()

    def test_create_user_existing(self):
        """Test user creation when user already exists"""
        existing_user = User(username="test_user", password="hashed_pwd", userhash="hash123")
        self.mock_session.query().filter().first.return_value = existing_user

        result = self.db_helper.create_user("test_user", "secure_password", "hash123")

        self.assertFalse(result)  # User already exists, should return False
 

    def test_hash_password(self):
        """Test password hashing"""
        hashed_password = self.db_helper.hash_password("secure_password")

        self.assertTrue(hashed_password.startswith("$2b$")) 

    def test_verify_password(self):
        """Test password verification"""
        hashed_password = self.db_helper.hash_password("secure_password")
        result = self.db_helper.verify_password("secure_password", hashed_password)

        self.assertTrue(result)
    
    def test_verify_password_fail(self):
        """Test password verification failure"""
        hashed_password = self.db_helper.hash_password("secure_password")
        result = self.db_helper.verify_password("wrong_password", hashed_password)

        self.assertFalse(result)    
    
    def test_get_user_password(self):
        """Test getting user password"""
        user = User(username="test_user", password="hashed_pwd", userhash="hash123")
        self.mock_session.query().filter().first.return_value = user

        result = self.db_helper.get_user_password("test_user")

        self.assertEqual(result, "hashed_pwd")
    
    def test_get_user_password_not_found(self):
        """Test getting user password when user not found"""
        self.mock_session.query().filter().first.return_value = None

        result = self.db_helper.get_user_password("test_user")

        self.assertIsNone(result)
    
    def test_update_user_password(self):
        """Test updating user password"""

        user = User(username="test_user", password= self.db_helper.hash_password("old_password"), userhash="hash123")
        self.mock_session.query().filter().first.return_value = user
        self.mock_session.commit = MagicMock()

        self.db_helper.hash_password = MagicMock(return_value="hashed_new_password")

        result = self.db_helper.update_user_password("test_user", "new_password")

        self.assertTrue(result)
        self.db_helper.hash_password.assert_called_once_with("new_password")  # Ensure hashing was called
        self.assertEqual(user.password, "hashed_new_password")  # Ensure updated password
        self.mock_session.commit.assert_called_once()

    
    def test_update_user_password_not_found(self):
        """Test updating user password when user not found"""
        self.mock_session.query().filter().first.return_value = None

        result = self.db_helper.update_user_password("test_user", "new_password")

        self.assertFalse(result)
    
    def test_delete_user(self):
        """Test deleting user"""
        user = User(username="test_user", password="hashed_pwd", userhash="hash123")
        self.mock_session.query().filter().first.return_value = user
        self.mock_session.commit = MagicMock()

        result = self.db_helper.delete_user("test_user")

        self.assertTrue(result)
        self.mock_session.delete.assert_called_once_with(user)
        self.mock_session.commit.assert_called_once()
    
    def test_delete_user_not_found(self):
        """Test deleting user when user not found"""
        self.mock_session.query().filter().first.return_value = None

        result = self.db_helper.delete_user("test_user")

        self.assertFalse(result)
    

