from board import SCL, SDA
import busio
from oled_text import OledText

def showText(text, line):
	i2c = busio.I2C(SCL, SDA)
	oled = OledText(i2c, 128, 64)
	oled.text(text, line)
