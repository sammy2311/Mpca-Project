import os
import json
import Pay
import time
import Display

def menu(choice):
    confirm = 'n'
    totalPrice = 0
    if(choice ==1): #print menu
        while(confirm == 'n'):
            os.system("clear")
            f = open("menu.json")
            data = json.load(f)
            size = len(data['menu'])
            print("\n\n\t\t\t--------------")
            for i, d in enumerate(data["menu"]):
                print(f"\t\t\t{i+1} - {d['name']} - {d['price']}") 
            print("\t\t\t--------------\n\n")
            print("Select items to buy (enter item number):")
            itemList = []
            item = input()
            while(item):
                if(int(item) > size):
                    print("not a valid item")
                else:
                    Display.showText(data['menu'][int(item)-1]['name'], 1)
                    itemList.append(int(item))
                    totalPrice += data['menu'][int(item)-1]['price']
                item = input()
            print("Selected items are: ", itemList)
            print("Total price", totalPrice)
            confirm = input("Confirm (y/n): ")
            text = "Total amount: "+str(totalPrice)
            Display.showText(text, 1)
            if(confirm=='n'):
                totalPrice = 0
                continue
            Pay.pay(totalPrice)
            time.sleep(3)
            Display.showText("Welcome to Canteen", 2)
            totalPrice = 0
            confirm = 'n'
        
    else:
        pass
        
    
