#!/usr/bin/env python3
"""
Python script provides some stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == '__main__':
    """The main namespace"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collections = client.logs.nginx
    print("{} logs".format(collections.count_documents({})))
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        counted = collections.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, counted))

    get_status_count = collections.count_documents(
        {"method": methods[0], "path": "/status"})
    print("{} status check".format(get_status_count))
