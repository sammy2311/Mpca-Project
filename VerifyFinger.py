import time
import board
import busio
import Display
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
import Client
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# uart = busio.UART(board.TX, board.RX, baudrate=57600)

# If using with a computer such as Linux/RaspberryPi, Mac, Windows with USB/serial converter:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)

# If using with Linux/Raspberry Pi and hardware UART:
import serial


def get_fingerprint(price):
    uart = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=1)
    finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    #print("Templating...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return 0, 0
    #print("Searching...")
    if finger.finger_search() != adafruit_fingerprint.OK:
        return 0, 0
    #i = finger.get_image()
    res = Client.sendData({'price':price, 'fingerid':finger.finger_id})
    return 1, finger.finger_id
    

