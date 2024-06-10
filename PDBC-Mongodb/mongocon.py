from pymongo import MongoClient
clients=MongoClient("mongodb://localhost:27017")
print("connection successfull")

db=clients['10am']
user_collection=db['users']
user_collection.insert_one({"eid":101,"ename":"sunil"})
print("data inserted succefully")