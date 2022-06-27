import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    client=None
    
    #init method gets you signed into database so you can start using it
    def __init__(self, username=None, password=None):       
        if username and password:
            self.client= MongoClient('mongodb://%s:%s@localhost:49286' % (username,password))
        else:
            self.client = MongoClient('mongodb://localhost:49286')
        self.database=self.client['project']
        
        # alows you to make a document and add it to database
        # data is Json formated document
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert!= 0:
                return True
            else:
                return False
        else:
            raise Exception("No input data")
            
            #allows you read from the database
            #criteria is joson fromated criteria for what you want to read
            # returns json formated document from database or error message
            # from mongo
    def read(self, criteria=None):
        if criteria:
            data = self.database.animals.find(criteria, {"_id":False})
        else:
            data=self.database.animals.find({}, {"_id":False})
        return data
    
    #used for updating documents in the database
    #takes two arguments the first is dictionary for finding the desired document
    #the second is the update command used for the update
    #returns mongo update message or error if fails to update
    def update(self, document1, document2):
        if document1 is not None and document2 is not None:
            update = self.database.animals.update(document1,document2)
            if update['n'] == 0:
                return("error: failed to update document")
            return update
            
            
    # deletes documents from the database
    # input is the dictionary to find desired document
    #returns error message if fails and the mongo return if success
    def delete(self, document):
        if document is not None:
            remove = self.database.animals.remove(document)
          
            if remove['n'] == 0:
                return("error: failed to remove document")
            return remove