import pymongo
from pymongo.mongo_client import MongoClient

uri='mongodb+srv://aryangaur556:Abhishek@cluster0.pfi4w9l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

class mongo_retriever: 
  def get_mongo_client(self, uri):
    try:
      client = MongoClient(uri)
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
      return client
    except Exception as e:
      print(e)
      return None
  
  def mongo_setup(self):
    mongo_client=self.get_mongo_client(uri)
    db=mongo_client["roomy"]
    collection=db["roomdata"]

    return collection

# Sample user data with latitude and longitude
# users = [
#     {'user': 'user1', 'Name': 'Alice', 'location': (37.7749, -122.4194), 'Budget': 3000, 'Hobbies': 'cricket,reading', 'Is_Vegetarian': True},
#     {'user': 'user2', 'Name': 'Bob', 'location': (34.0522, -118.2437), 'Budget': 2000, 'Hobbies': 'reading,music', 'Is_Vegetarian': False},
#     {'user': 'user3', 'Name': 'Charlie', 'location': (40.7128, -74.0060), 'Budget': 4000, 'Hobbies': 'reading,music', 'Is_Vegetarian': True},
#     {'user': 'user4', 'Name': 'David', 'location': (37.7759, -122.4194), 'Budget': 3500, 'Hobbies': 'movies,travel', 'Is_Vegetarian': False},
# ]

# mret = mongo_retriever()
# collection = mret.mongo_setup()
# collection.insert_many(users)