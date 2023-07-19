#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

"""
Writing strings to Redis
Contains the Cache class
"""


def count_calls(method: Callable) -> Callable:
    """
    A wrapper function that counts the amount of time a function is
    called. Saves the number to redis
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"
        Wrapper function
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    A wrapper function that records the call history of a function
    with redis.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A wrapper function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


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

    @count_calls
    @count_history
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
