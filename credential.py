import random

class Credentials:
    '''
    Class credentials to generate new instances of user credentials 
    '''

    credentials_list = []

    def __init__(self, account, login, password, confirm_password):
        self.account = account
        self.login = login
        self.password = password
        self.confirm_password = confirm_password

    def save_credentials(self):
        '''
        Save_credentials saves credentials object to credentials_list
        '''

    @classmethod
    def display_credentials(cls):
        '''
        Display credentials to show the credential list
        '''
        return cls.credentials_list