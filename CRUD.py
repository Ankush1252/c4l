db.createCollection("myNewDatabase")
use myNewDatabase 

db.myNewCollection.insertOne({name: "Ankush Awate", age: 30})
db.myNewCollection.insertOne({name: "Shantanu Sawandkar", age: 25}) 
db.myNewCollection.insertMany([{name: "Shivam", age: 28}, {name: "Rajesh Sawant", age: 32}]) 

db.myNewCollection.findOne({name: "Ankush Awate"}) 
db.myNewCollection.find({age: {$gt: 25}})

db.myNewCollection.updateOne({name: "Ankush Awate"}, {$set: {age: 31}}) 

db.myNewCollection.updateMany({age: {$gt: 30}}, {$set: {status: "senior"}}) 

db.myNewCollection.deleteOne({name: "Rajesh Sawant"}) 

db.myNewCollection.deleteMany({status: "senior"}) 

db.myNewCollection.find()