#!/usr/bin/env python3
"""
Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    update_topics:
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
