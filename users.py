import pyperclip

class User:
    '''
    User class for user input 
    '''

    user_list = [] # User Empty list

    def __init__(self, first_name, last_name, phone_number, email):        

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


    def save_user(self):

        '''
        save_usermethod saves user objects into user_list
        '''

        User.user_list.append(self)


        

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)


    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            user that matches the number.
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user



