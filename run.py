#!/usr/bin/env python3.6
from user import User
from credential import Credentials
import random

# 1. Creating a User


def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

# 2. Save user


def save_users(user):
    '''
    Function to save user
    '''
    User.save_user()


def new_credentials(account, login, password, confirm_password):
    '''
   function for user to create new credentials
   '''
    new_credentials = Credentials(account, login, password, confirm_password)
    return new_credentials


def save_credentials(credential):
    '''
    function to save user credentials
    '''
    credential.save_credential()

# 3. Delete user


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

# 5. Check if a user exists


def check_existing_users(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)


# 6. Displaying all contacts
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()


def display_credentials():
    '''
    Function to display credential list
    '''
    return Credentials.display_credentials()


def main():
    print("Hello! Welcome to Password Manager. What is your name?")
    username = input()
    print("\n")
    print(f"Hi There {username}.")

    while True:

        print("\nUse the short codes below to interact with the App:")
        print("."*40)
        print("\n dc - Display Credentials ca - Create an Account, cc - Create Credentials, gp - Generate Password, cp - Create Password, ex - exit Password Manager")

        short_code = input().lower()

        if short_code == 'ca':
            print("New User Account")
            print("."*14)

            print("\nEnter your Username")
            print("."*40)
            username = input()

            print("\nEnter your Password")
            print("."*40)
            password = input()

            save_users(create_user(username, password))

            print("\n")
            print("New User {username} Created.\n")

        elif short_code == 'cc':
            print("\nLogin to your Account")
            print("."*40)
            print("\nUsername?")
            print("." * 20)
            username = input()
            print("\nPassword?")
            print("."*20)
            password = input()
            confirm_password = password
            if check_existing_users(password):
                print("\nWelcome back!")
                print("New Credential")
                print("." * 20)

                print("\nWhich account do the credentials belong to?")
                print("."*40)
                account = input()

                print("\nWhat's your login name for the {account} account?")
                print("."*40)
                login_name = input()

                print("\nChoose:")
                print("."*20)
                print("'gp' - program to generate your password for you, 'cp' - create your own password")
                password_creation_input = input()
            if password_creation_input == "cp":
                print("\nEnter your password")
                print("."*20)
                password = input()
            elif password_creation_input == "gp":
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                password = "".join(random.choice(chars) for _ in range(8))
                print("\nYour password is: **{password}**")

                save_credentials(new_credentials(account, login_name, password, confirm_password))
                print("\n")
                print(
                    "New credentials {account}, {login_name}, {password} created")

            else:
                print("Wrong password or username. Please Try again.\n Username?")
                print("."*20)
                username = input()
                print("\nPassword?")
                print("."*20)
                password = input()
            if check_existing_users(password):
                print("\nWelcome back!")
            else:
                print("You don't have an account.\n")

        elif short_code == 'dc':
            if display_credentials():
                for credential in display_credentials():
                    print(
                        "\nAccount: {credential.account}\nLogin Name: {credential.login}\nAccount Password: {credential.password}")
            else:
                print("\n You don't seem to have any credentials saved yet")

        elif short_code == 'ex':
            print("."*50)
            print("Thank you for using Pass-locker...")
            print("."*50)
            break

        else:
            print("Sorry, I didn't get that. Please use the short codes\n")


if __name__ == '__main__':
    main()
