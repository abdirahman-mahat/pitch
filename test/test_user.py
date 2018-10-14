import unittest
from app.models import User
class UserModelTest(unittest.TestCase):
    def setUp(self):
    # method creates new instance of user 
        self.new_user = User(password = 'marcus')
    def test_password_setter(self):
    # method that ascertains that when password is being hashed and the pass_secure contains a value
        self.asserTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
    # method that confirms that our application raises an AttributeError when we try to access the password property 
        with self.assertRaises(AttributeError):
            self.new_user.password
    def test_password_verification(self):
        # method that confirms that our password hash can be verified when we pass in the correct password 
            self.asserTrue(self.new_user.verify_password('marcus'))


