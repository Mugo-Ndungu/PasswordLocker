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



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.last_name,"Muriuki")


    def test_save_user(self):
        '''
        test_save_contact test case to test if the user object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new conusertact
        self.assertEqual(len(User.user_list),1)

