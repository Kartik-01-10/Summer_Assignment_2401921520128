
# ## What is MongoDB?
# MongoDB is a NoSQL database that stores data in flexible, JSON-like documents. It is widely used for handling large volumes of 
# unstructured data.

# ## Why Use MongoDB with Python?
# Python can interact with MongoDB using the `pymongo` library. This allows you to store, retrieve, and manage data easily from 
# your Python programs.


## Steps to Use MongoDB with Python

### 1. Install pymongo
# First, install the `pymongo` library using the terminal in VS Code:

# pip install pymongo


## Connect to MongoDB
# Use `MongoClient` to connect to your MongoDB server.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")


# Install pymongo if not already installed
# pip install pymongo


# 🗂️ 2. Create or access a database
db = client["school_db"]

# 📁 3. Create or access a collection (like a table)
students = db["students"]
# basic difference btw database amd collection
# - Database → Like a folder 📁
# It’s the container that holds multiple collections.
# - Collection → Like a file 📄
# It’s where the actual data (documents) is stored.
# - So yes:
# - You first create a database, which acts as the environment.
# - Then you create collections inside that database to store your data.


# 🧹 4. Delete all documents (for clean testing)
students.delete_many({})

# 📝 5. Insert one document
students.insert_one({
    "name": "Kartik",
    "age": 21,
    "courses": ["Python", "SQL"],
    "score": 88
})

# 📥 6. Insert multiple documents
students.insert_many([
    {"name": "Amit", "age": 22, "courses": ["Java"], "score": 75},
    {"name": "Neha", "age": 20, "courses": ["Python", "Flask"], "score": 92}
])

# 🔍 7. Find one document
one_student = students.find_one({"name": "Kartik"})
print("Find One:", one_student)

# 🔎 8. Find all documents i.e if i want to print all data
for student in students.find():
    print("Find All:", student)

# 🔎 9. Find with condition and projection
for student in students.find({"age": {"$gt": 20}}, {"_id": 0, "name": 1, "score": 1}):
    print("Filtered:", student)

# ✏️ 10. Update one document  -- - Even if multiple documents match, only one gets updated.
students.update_one({"name": "Amit"}, {"$set": {"score": 80}})

# ✏️ 11. Update multiple documents
students.update_many({"courses": "Python"}, {"$inc": {"score": 5}})
# - A document is a single record of data.
# - It’s stored inside a collection.
# - It’s written in BSON format (Binary JSON), which looks like a Python dictionary.
"""
📌 MongoDB Update Operators (Used in update_one / update_many)

| Operator     | Purpose                                      | Example Usage                        |
|--------------|----------------------------------------------|--------------------------------------|
| $set         | Set or replace a field value                 | {"$set": {"score": 90}}              |
| $inc         | Increment a numeric field                    | {"$inc": {"score": 5}}               |
| $mul         | Multiply a numeric field                     | {"$mul": {"score": 2}}               |
| $rename      | Rename a field                               | {"$rename": {"oldName": "newName"}}  |
| $unset       | Remove a field from the document             | {"$unset": {"score": ""}}            |
| $min         | Set value only if it's lower than current    | {"$min": {"score": 80}}              |
| $max         | Set value only if it's higher than current   | {"$max": {"score": 95}}              |
| $currentDate | Set field to current date/time               | {"$currentDate": {"lastModified": True}} |
"""

# ❌ 12. Delete one document
students.delete_one({"name": "Neha"})

# ❌ 13. Delete multiple documents
students.delete_many({"score": {"$lt": 80}})

# 📊 14. Count documents
print("Total Students:", students.count_documents({}))

# 📊 15. Aggregation (e.g., average score)
pipeline = [
    {"$group": {"_id": None, "avg_score": {"$avg": "$score"}}}
]
for result in students.aggregate(pipeline):
    print("Average Score:", result["avg_score"])

# 📌 16. Create index
students.create_index("name")

# 📌 17. List indexes
print("Indexes:", students.index_information())

# 🧪 18. Drop collection 
# students.drop()

# 🧪 19. Drop database -->> means delete the entire database 
# client.drop_database("school_db")

# ✅ 20. Close connection
client.close()

"""
📚 MongoDB Function Summary (Python + pymongo)

🔗 CONNECTION
| Function                  | Purpose                          |
|---------------------------|----------------------------------|
| MongoClient(uri)          | Connect to MongoDB server        |
| client.close()            | Close the connection             |

🗂️ DATABASE & COLLECTION
| Function                  | Purpose                          |
|---------------------------|----------------------------------|
| client["db_name"]         | Access or create database        |
| db["collection_name"]     | Access or create collection      |

📝 INSERT
| Function                  | Purpose                          |
|---------------------------|----------------------------------|
| insert_one(doc)           | Insert a single document         |
| insert_many([docs])       | Insert multiple documents        |

🔍 READ / FIND
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| find_one(filter)                          | Find first matching document     |
| find(filter)                              | Find all matching documents      |
| find(filter, projection)                  | Filter + select specific fields  |

✏️ UPDATE
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| update_one(filter, update)                | Update first matching document   |
| update_many(filter, update)               | Update all matching documents    |

❌ DELETE
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| delete_one(filter)                        | Delete first matching document   |
| delete_many(filter)                       | Delete all matching documents    |

📊 COUNT & AGGREGATION
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| count_documents(filter)                   | Count matching documents         |
| aggregate(pipeline)                       | Perform aggregation operations   |

📌 INDEXING
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| create_index("field")                     | Create index on field            |
| index_information()                       | List all indexes                 |

🧹 CLEANUP
| Function                                  | Purpose                          |
|-------------------------------------------|----------------------------------|
| collection.drop()                         | Drop the collection              |
| client.drop_database("db_name")           | Drop the database                |
"""

"""
📚 MongoDB Operators Cheat Sheet


🔍 QUERY OPERATORS (used in find / find_one)
| Operator       | Purpose                                 |
|----------------|-----------------------------------------|
| $eq            | Equal to                                |
| $ne            | Not equal to                            |
| $gt            | Greater than                            |
| $lt            | Less than                               |
| $gte           | Greater than or equal to                |
| $lte           | Less than or equal to                   |
| $in            | Matches any value in array              |
| $nin           | Matches none of the values in array     |
| $and           | Combine multiple conditions (AND)       |
| $or            | Combine multiple conditions (OR)        |
| $not           | Negate a condition                      |
| $exists        | Check if field exists                   |
| $type          | Match field by BSON type                |
| $regex         | Match using regular expression          |

📊 AGGREGATION OPERATORS (used in aggregate pipelines)
| Operator       | Purpose                                 |
|----------------|-----------------------------------------|
| $match         | Filter documents                        |
| $group         | Group and aggregate data                |
| $project       | Include/exclude fields                  |
| $sort          | Sort documents                          |
| $limit         | Limit number of results                 |
| $skip          | Skip number of documents                |
| $count         | Count documents                         |
| $sum           | Sum values                              |
| $avg           | Average values                          |
| $min / $max    | Min or max values                       |
| $push / $addToSet | Add values to array in grouping      |

📦 ARRAY OPERATORS (used in updates or queries)
| Operator       | Purpose                                 |
|----------------|-----------------------------------------|
| $push          | Add item to array                       |
| $pull          | Remove item from array                  |
| $addToSet      | Add item only if not already present    |
| $pop           | Remove first or last item               |
| $each          | Push multiple items                     |
| $size          | Match array size                        |
| $elemMatch     | Match array element with condition      |
"""

# $bit: Bitwise AND operation
students.update_one({"name": "Kartik"}, {"$bit": {"flags": {"and": 5}}})

# $text: Full-text search (requires text index)
students.create_index([("description", "text")])
students.find({"$text": {"$search": "MongoDB"}})

# $lookup: Join with another collection
db.orders.aggregate([
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "_id",
            "as": "product_info"
        }
    }
])


from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mixed_data"]

# Insert multiple documents with different formats
collection.insert_many([
    # Simple document with string and number
    {"name": "Kartik", "age": 22},

    # Document with array
    {"name": "Amit", "skills": ["Python", "MongoDB", "Flask"]},

    # Document with nested object
    {"name": "Neha", "address": {"city": "Delhi", "zip": 110001}},

    # Document with boolean and null
    {"name": "Ravi", "active": True, "email": None},

    # Document with mixed types
    {
        "name": "Priya",
        "projects": [
            {"title": "API Dev", "status": "completed"},
            {"title": "DB Integration", "status": "ongoing"}
        ],
        "score": 87.5,
        "verified": False
    }
])

# second method 
data = [
    # Simple document with string and number
    {"name": "Kartik", "age": 22},

    # Document with array
    {"name": "Amit", "skills": ["Python", "MongoDB", "Flask"]},

    # Document with nested object
    {"name": "Neha", "address": {"city": "Delhi", "zip": 110001}},

    # Document with boolean and null
    {"name": "Ravi", "active": True, "email": None},

    # Document with mixed types
    {
        "name": "Priya",
        "projects": [
            {"title": "API Dev", "status": "completed"},
            {"title": "DB Integration", "status": "ongoing"}
        ],
        "score": 87.5,
        "verified": False
    }
]
collection.insert_many(data)
#third method 
# we can also use insert_one using for loop 

documents = [
    {"name": "Kartik", "age": 22},
    {"name": "Amit", "skills": ["Python", "MongoDB", "Flask"]},
    {"name": "Neha", "address": {"city": "Delhi", "zip": 110001}},
    {"name": "Ravi", "active": True, "email": None},
    {
        "name": "Priya",
        "projects": [
            {"title": "API Dev", "status": "completed"},
            {"title": "DB Integration", "status": "ongoing"}
        ],
        "score": 87.5,
        "verified": False
    }
]

# Insert each document individually
for doc in documents:
    collection.insert_one(doc)

