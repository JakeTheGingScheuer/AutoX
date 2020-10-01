from pymongo import MongoClient


class MongoWrapper:

    def __init__(self, db_name: str):
        self.client = MongoClient()
        self.current_db = db_name
        self.current_collection = None

    def use_database(self, db_name):
        self.current_db = db_name

    def use_collection(self, collection_name):
        self.current_collection = collection_name

    def list_databases(self):
        return self.client.list_databases()

    def list_collections(self):
        return self.client[self.current_db].list_collections()

    def insert_one(self, document):
        return self.client[self.current_db][self.current_collection].insert_one(document)

    def find(self, query_object):
        return self.client[self.current_db][self.current_collection].find(query_object)

    def find_one(self, query_object):
        return self.client[self.current_db][self.current_collection].find_one(query_object)

    def drop_collection(self, collection_name):
        return self.client[self.current_db][collection_name].drop()
