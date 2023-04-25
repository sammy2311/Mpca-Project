import os 
import VerifyFinger
import Display

def pay(price):
    count = 5
    res = 0
    while(~res and count):
        
        count = count-1
        res, i = VerifyFinger.get_fingerprint(price)
        if(res == 1):
            break
        else:
            Display.showText("Could not find a match", 2)
            Display.showText("try again..", 4)

