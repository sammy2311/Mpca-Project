import os
import Login 
import Menu
import Display

os.system("clear")
print("Welcome to PES!!")
Display.showText("Welcome to PES",1)
print("1. Login")
print("2. Register")
choice = int(input("Enter your choice: "))
if(choice == 1):
   choice = Login.login()
   Menu.menu(choice)
