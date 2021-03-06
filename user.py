class User:
    '''
    User class for user input 
    '''

    user_list = [] # User Empty list

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
    
        '''
        save_usermethod saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def user_exists(cls, characters):
        '''
        Method to che if a user exists

        args:
            character:username to search if it exist

        return:
            Boolean: true or false depending o the search outcome
        '''

        for user in cls.user_list:
            if user.password == characters:
                return True

        return False