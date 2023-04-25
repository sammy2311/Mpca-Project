import requests

url='http://127.0.0.1:5000/'
def sendData(obj):
	x = requests.post(url, json = obj)
	print(x.text)

