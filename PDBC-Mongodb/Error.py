import requests
from pymongo import MongoClient
resp=requests.get("https://jsonplaceholder.typicode.com/users")
user_list=resp.json()

try:
    clients=MongoClient("mongodb://localhost:27017")
    print("Mongodb connected successfully")
    db=clients["12pm"]
    user_collection=db['users']
    user_collection.insert_many(user_list)
    print("data inserted succesfully")

except:
    print("doesnt connected to mongodb") 

finally:
    user_collection=None
    db=None
    clients=None       