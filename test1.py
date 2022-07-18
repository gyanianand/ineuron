import pymongo

client = pymongo.MongoClient("mongodb+srv://gyan3690:Gyan123@cluster0.dd3sr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"sudh",
    "email":"su@s.com",
    "surname":"kumar"
}

db1=client['mongotest']
col=db1['test']
col.insert_one(d)


d1={
    "name":"sudh",
    "email":"su@s.com",
    "surname":"kumar"
}

db1=client['mongotest']
col=db1['test']
col.insert_one(d)