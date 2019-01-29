import unittest # Importing the unittest module
from users import User # Importing the user class
import pyperclip



class TestUser(unittest.TestCase):
    """
    Args:
    username = new username
    password = new password
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

        '''
        Test class that defines test cases for the contact class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","0712345678","james@ms.com") # create user object
