import unittest  # Importing the unittest module
from user import User  # Importing the user class


class TestUser(unittest.TestCase):
    """
    Args:
    username = new username
    password = new password
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James", "james123")  # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username, "James")
        self.assertEqual(self.new_user.password, "james123")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the users' list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    # def test_save_multiple_user(self):
    #     '''
    #     test_save_multiple_user to check if we can save multiple user
    #     objects to our user_list
    #     '''
    #     self.new_user.save_user()
    #     test_user = Users("User", "1234")  # new user
    #     test_user.save_user()
    #     self.assertEqual(len(User.user_list), 2)

    # def test_delete_user(self):
    #         '''
    #         test_delete_user to test if we can remove a user from our user list
    #         '''
    #         self.new_user.save_user()
    #         test_user = User("User","1234") # new user
    #         test_user.save_user()
    #
    #         self.new_user.delete_user()# Deleting a user object
    #         self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        """
        test_user_exists test case to check if we can return a boolean if we cannot find the user
        """
        self.new_user.save_user()
        test_user = User("User", "12345")
        test_user.save_user()
        user_exists = User.user_exists("12345")
        self.assertTrue(user_exists)

    # def test_display_all_users(self):
    #     '''
    #     method that returns a list of all user saved
    #     '''
    #
    #     self.assertEqual(User.display_user(), User.user_list)


if __name__ == '__main__':
    unittest.main()
