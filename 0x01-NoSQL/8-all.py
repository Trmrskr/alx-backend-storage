#!/usr/bin/python3
""" Python script that List all documents in Python
   Prototype: def list_all(mongo_collection)
   Returns an empty list if no document in the collection
   mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """
    list_all - takes a collection object and returns a list of documents
    @mongo_collection: a collection object
    returns documents from a collection.
    """

    if mongo_collection is None:
        return []
    collections = mongo_collection.find()
    
    if not collections:
        return []
    return [collection for collection in collections]
