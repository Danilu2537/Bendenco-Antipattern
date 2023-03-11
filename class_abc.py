from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    def __init__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, title, qty):
        pass

    @abstractmethod
    def remove(self, title, qty):
        pass

    @property
    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass
