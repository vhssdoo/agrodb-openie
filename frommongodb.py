import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["agroecology"]

customers = db["abstracts"]

for n, x in enumerate(customers.find()):
    #print(x)
    print(n, x["db_id"], "\t", x["title"])
