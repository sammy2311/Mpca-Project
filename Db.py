import Display
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://strawberriessss:berriessss@mpca.vzofeaw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.MPCA
collection = db.users

def insert(obj):
    i = collection.insert_one(obj)
    print("inserted", i)
    
def find(obj):
    record = collection.find_one(obj)
    return record
    
def update(price, obj):
    record = find(obj)
    print(record)
    curr = record['balance']
    if(curr-price>=0):
        collection.update_one(record, {"$set":{"balance":curr-price}})
        Display.showText("PAID SUCCESSFULLY", 2)
        return "1"
    else:
        Display.showText("NOT ENOUGH BALANCE", 2)
        return "0"
                
def delete(i):
    collection.delete_one({'fingerid': i})

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
