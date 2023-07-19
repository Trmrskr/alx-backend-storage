#!/usr/bin/env python3
import redis
import uuid
from typing import Union

"""
Writing strings to Redis
Contains the Cache class
"""


class Cache:
    """
    Cache class
    contains the __init__ constructor and store method
    """
    def __init__(self):
        """
        class constructor
        initialize and flush redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store method
        Create key, set to redis and returns key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
