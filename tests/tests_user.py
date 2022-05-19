import unittest

from app.models import *

class TestUsers(unittest.TestCase):

    def setUp(self):
        """
        This will create an instance of the User before each test case
        """
        self.new_user = User(username='adele',email = "muscify@test.com", bio ='default bio',password='stac101')
    
    def tearDown(self):
        """
        Will delete all the info from the db
        """
        User.query.delete()
        Review.query.delete()

    
    def test_instance(self):
        """
        Will test whether the new instance is an instance of the User model
        """
        self.assertTrue(isinstance(self.new_user, User))
       
    
    def test_init(self):
        """
        Will test whether the User model is instantiated correctly
        """
        self.assertEqual(self.new_user.username,"adele")


    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

                
    def test_password_is_hashed(self):
        """
        Will test whether the password generated is not equal to the inputted password
        """
        self.assertTrue(self.new_user.password_hash is not "stac101")

    def test_password_verifier(self):
        """
        Will test whether the user can decrypt the password with their password
        """
        self.assertTrue(self.new_user.verify_password("stac101"))




      

     




    

