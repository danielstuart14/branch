"""
BranchDB - A Multilevel Database

Example File

Author: Daniel P. Stuart
"""
import branch
import json

server = "" # Insert here your server URL
name = "test" # Database name (It'll be created by BranchDB)

db = branch.connect(server, name) # Starts connection

# 1 - Creates an object/document
id = db.createObject('{"Name": "Test 1"}')
# 2 - Creates an affiliated collection 
id2 = db.createChild(id)
# 3 - Selects collection (optional, you can execute a command in a specific collection with an argument, see step 6)
db.selectCollection(id2)
# 4 - Creates a new object/document inside the selected collection
id3 = db.createObject('{"Name": "Test 2"}')
# 5 - Creates an affiliated collection 
id4 = db.createChild(id3)
# 6 - Creates a new object/document inside collection id4
id5 = db.createObject('{"Name": "Test 3"}', id4)

# 6 - Gets id3's child and compares if equal to id4
if db.getChild(id3, id2) == id4:
    print(" id3's child is equal to id4")

# 7 - Prints data in id5
print(db.readObject(id5, id4))
# 8 - Updates id5 and prints it again
db.updateObject(id5, '{"Name": "Test 4"}', id4)
print(db.readObject(id5, id4))
# 9 - Checks if there is an object with name Test 4 at id4
if db.searchObject('{"Name": "Test 4"}',id4) != None:
    print("Object with name Test 4 exists at id4")
# 10 - Deletes id5
db.deleteObject(id5, id4)

# 10 - Checks if id, id2, id3 and id4 are ancestors of something
if db.isAncestor(id, "root"):
    print("object id at root collection is an ancestor")
if db.isAncestor(id2):
    print("collection id2 is an ancestor")
if not(db.isAncestor(id3, id2)):
    print("Object id3 is not an ancestor") 
if not(db.isAncestor(id4)):
    print("collection id4 is not an ancestor") 
# 11 - Selects id4 and prints its path
db.selectCollection(id4)
print(db.getPath())

# 12 - Deletes id3 child (id4)
db.deleteChild(id3, id2)

# 13 - Prints all collections
print(db.getCollections())
