import unittest
from credential import Credentials


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credentials(
            "123456", "instagram", "milkshake", "12345")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run
        '''
        Credentials.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account, "instagram")
        self.assertEqual(self.new_credential.login, "milkshake")
        self.assertEqual(self.new_credential.password, "paula1234")
        self.assertEqual(self.new_credential.confirm_password, "paula1234")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saves into
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if one can save multiple credentials
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("test","login","67890","12345")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_display_all_credentials(self):
        '''
        test_display_all_credentials to returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    if __name__ == '__main__':
        unittest.main()