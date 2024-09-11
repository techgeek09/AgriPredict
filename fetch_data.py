from pymongo import MongoClient 
connection_string= "mongodb+srv://anamabdin910:FpMFZoQoi8Czvtnv@farmerproject.sy12i.mongodb.net/?retryWrites=true&w=majority&appName=farmerproject"
client = MongoClient(connection_string)
database = client['Farmer2']
collection = database['FarmerData1']

documents = collection.find()  # select * from table;
for document in documents: 
    print(document) 
print("thank you!") 

# execute this file to fectch your data from database 