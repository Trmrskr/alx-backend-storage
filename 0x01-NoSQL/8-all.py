#!/usr/bin/python3
""" List all documents in Python """


def list_all(mongo_collection):
    """
    list_all - takes a collection object and returns a list of documents
    @mongo_collection: a collection object
    returns documents from a collection.
    """
    collections = mongo_collection.find()
    
    if not collections:
        return []
    return [collection for collection in collections]
