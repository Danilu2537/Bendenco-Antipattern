from class_base_storage import BaseStorage
from exceptions import NotEnoughSpace, MaxUniqueItemsInStorage


class Shop(BaseStorage):
    """
    Магазин товаров
    """

    def __init__(self):
        super().__init__()
        self._capacity = 20
        self.max_unique_items = 5

    def __repr__(self):
        if len(self.get_items) == 0:
            return f'В магазине пусто! Вместимость: {self._capacity}.'
        return 'В магазине хранятся:\n' + '\n'.join(f'> {amount} {item}' for item, amount in self.get_items.items())

    def add(self, title: str, qty: int) -> None:
        if not self.get_free_space() >= qty:
            raise NotEnoughSpace()

        if self.get_unique_items_count() == self.max_unique_items and title not in self.get_items:
            print(f'В магазине уже {self.max_unique_items} видов различных товаров.')
            raise MaxUniqueItemsInStorage()

        if title not in self.get_items:
            self._items[title] = 0
        self._items[title] += qty
