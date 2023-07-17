#!/usr/bin/python3
"""Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    insert_school - insert kwargs into mongo_collection
    @mongo_collection: the collection to be inserted into
    @kwargs: the documents to be inserted
    Return: returns the new id
    """

    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
