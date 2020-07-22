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

    def create_index(self, index_object):
        return self.client[self.current_db][self.current_collection].create_index(index_object, unique=True)

    def list_databases(self):
        return self.client.list_databases()

    def list_collections(self):
        return self.client[self.current_db].list_collections()

    def get_index_info(self):
        return self.client[self.current_db][self.current_collection].index_information()

    def insert_one(self, document):
        return self.client[self.current_db][self.current_collection].insert_one(document)

    def find(self, query_object):
        return self.client[self.current_db][self.current_collection].find(query_object)

    def find_one(self, query_object):
        return self.client[self.current_db][self.current_collection].find_one(query_object)

    def drop_database(self, test_db_name):
        return self.client.drop_database(test_db_name)

    def drop_collection(self, collection_name):
        return self.client[self.current_db][collection_name].drop()

    def delete_one(self, query_object):
        return self.client[self.current_db][self.current_collection].delete_one(query_object)

    def update_one(self, query_object, update_object, upsert: bool = False):
        return self.client[self.current_db][self.current_collection].update_one(query_object, update_object, upsert=upsert)

    def replace_one(self, filter_object, replacement_object, upsert: bool = False):
        return self.client[self.current_db][self.current_collection].replace_one(filter_object, replacement_object, upsert=upsert)

    def get_total_documents(self, matcher=None):
        if matcher is None:
            matcher = {}
        return self.client[self.current_db][self.current_collection].count_documents(matcher)
