#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable

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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get data from the cache
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get a string from the cache
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        Get a int from the cache
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except:
            value = 0
        return value
