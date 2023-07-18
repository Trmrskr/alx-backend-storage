#!/usr/bin/env python3
"""MongoDB Operations with python using pymongo"""


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    top_student = mongo_collection.aggregrate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
