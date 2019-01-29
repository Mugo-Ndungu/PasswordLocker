#!/usr/bin/env python3.6
from users import User
import random



def __init__(self, username, password):
        self.username = username
        self.password = password

        """
        Args:
        username = new username
        password = new password
        """

#1. Creating a User
def create_user(first_name,last_name,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,phone,email)
    return new_user

#2. Save user
def save_users(user):
    '''
    Function to save user
    '''
    User.save_user()


#3. Delete user
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


#4. Finding a user
def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)


#5. Check if a user exists
def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)


#6. Displaying all contacts
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def main():
    print("Hello Welcome to your User list. What is your name?")
            user_name = input()
            print("Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("Phone number ...")
                            phone_number = input()

                            print("Email address ...")
                            email_address = input()


                            save_users(create_user(first_name,last_name,phone_number,email_address)) # create and save new user.
                            print ('\n')
                            print("New User {first_name} {last_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for contact in display_users():
                                            print("{user.first_name} {user.last_name} .....{user.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_users(search_number):
                                    search_user = find_user(search_number)
                                    print("{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print("Phone number.......{search_user.phone_number}")
                                    print("Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that.Please use the short codes")
if __name__ == '__main__':
main()