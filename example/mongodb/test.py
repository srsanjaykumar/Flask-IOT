from pymongo import MongoClient

client = MongoClient('mongodb://sanjay:cxdh1ssccb@mongodb.selfmade.ninja:27017/?authSource=users')
db = client.sanjay_iotcloud
 # db = client['sanjay_iotcloud']  alternative way

result = db.test.find_one({
    "username":"sanjaykumar"
})
print(result)








