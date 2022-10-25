import pprint
import pymongo

# connection
try:
	client = pymongo.MongoClient()
	db = client['test']
	print('connection to the server established')
	
except Exception:
	print('Failed to Connect to server')

collection = db.students


# creating an index
resp = collection.create_index("newIndex")

# printing the auto generated name
# returned by MongoDB
print(resp)

# index_information() is analogous
# to getIndexes
pprint.pprint(collection.index_information())

