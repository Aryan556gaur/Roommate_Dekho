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