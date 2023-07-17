#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """
    schools by topic
    """
    school_list = mongo_collection.find({"topics": topic})
    return [list for list in school_list]
