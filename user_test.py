import unittest # Importing the unittest module
from user import Users # Importing the user class
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
        Users.user_list = []

        '''
        Test class that defines test cases for the contact class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("James","Muriuki","0727774858","james@ms.com") # create user object



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.phone_number,"0727774858")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.last_name,"Muriuki")


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new conusertact
        self.assertEqual(len(Users.user_list),1)

    
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = Users("Test","user","0727774858","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(Users.user_list),2)

    
    
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = Users("Test","user","0727774858","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(Users.user_list),1)



    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = Users("Test","user","0720863011","test@user.com") # new user
        test_user.save_user()

        found_user = Users.find_by_number("0720863011")

        self.assertEqual(found_user.email,test_user.email)



    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_USER = Users("Test","user","0720863011","test@user.com") # new user
        test_USER.save_user()

        user_exists = Users.user_exist("0720863011")

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(Users.display_user(),Users.user_list)

if __name__ == '__main__':
    unittest.main()