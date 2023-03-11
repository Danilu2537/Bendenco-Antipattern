from class_abc import AbstractStorage
from exceptions import NotEnoughSpace, NotEnoughGoods, NoGoodsInStorage


class BaseStorage(AbstractStorage):
    """
    Базовый класс для складов и магазинов
    """

    def __init__(self):
        super().__init__()

    def add(self, title: str, qty: int) -> None:
        if not self.get_free_space() >= qty:
            raise NotEnoughSpace()

        if title not in self.get_items:
            self._items[title] = 0
        self._items[title] += qty

    def remove(self, title: str, qty: int) -> None:
        if title not in self.get_items:
            raise NoGoodsInStorage()

        if qty > self.get_items[title]:
            raise NotEnoughGoods()

        self.get_items[title] -= qty
        if self.get_items[title] == 0:
            del self._items[title]

    @property
    def get_items(self) -> dict[str: int]:
        return self._items

    def get_free_space(self) -> int:
        return self._capacity - sum(self.get_items.values())

    def get_unique_items_count(self) -> int:
        return len(self.get_items)
