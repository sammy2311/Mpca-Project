import os

def login():
    os.system("clear")
    print("Enter Credentials")
    user = str(input("Enter name: "))
    '''Check user in file'''
    password = str(input("Enter password: "))
    '''validate'''
    os.system("clear")
    print("LOGIN SUCCESSFULL")
    print("1. View Menu")
    print("2. Edit Menu")
    choice = int(input("Enter your choice"))
    return choice
