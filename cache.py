# author fangyh

import os
import torch
from abc import ABCMeta, abstractmethod


class DataBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class Cache:
    """
    At 1st call, it will store the object persistently.
    From 2nd call, it will return the stored object.

    Example:
        class TrainDatabase(DataBase):
            def get_data(self):
                ...
                return data
        cache = Cache("/home/persistent/")
        cache.fetch("train", TrainDatabase())
    """
    def __init__(self, cache_path):
        self.cache_path = cache_path

    def fetch(self, name, database):
        save_path = os.path.join(self.cache_path, name)
        if os.path.exists(save_path):
            return torch.load(save_path)
        else:
            data = database.get_data()
            torch.save(data, save_path)
            return data