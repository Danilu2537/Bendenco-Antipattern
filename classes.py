from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self):
        self._items = {}
        self._capacity = 0

    @abstractmethod
    def add(self, title, qty):
        pass

    @abstractmethod
    def remove(self, title, qty):
        pass

    @abstractmethod
    def delete_item(self, title):
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


class Store(Storage):
    """
    Класс склада товаров
    """

    def __init__(self):
        super().__init__()
        self._capacity = 100

    def __repr__(self):
        if len(self.get_items) == 0:
            return f'На складе пусто! Вместимость: {self._capacity}.'
        return 'На складе хранятся:\n' + '\n'.join(f'> {amount} {item}' for item, amount in self.get_items.items())

    def add(self, title: str, qty: int) -> bool:
        if self.get_free_space() >= qty:
            if title not in self.get_items:
                self._items[title] = 0
            self._items[title] += qty
            return True
        else:
            print(f'На складе недостаточно места!\n')
        return False

    def remove(self, title: str, qty: int) -> bool:
        if title in self.get_items:
            if qty <= self.get_items[title]:
                self.get_items[title] -= qty
                if self.get_items[title] == 0:
                    self.delete_item(title)
                return True
            else:
                print(f'Не достаточно товара "{title}" на складе! Попробуйте заказать меньше!\n')
        else:
            print(f'Данного товара нет на складе!\n')
        return False

    def delete_item(self, title):
        del self._items[title]

    @property
    def get_items(self) -> dict[str: int]:
        return self._items

    def get_free_space(self) -> int:
        return self._capacity - sum(self.get_items.values())

    def get_unique_items_count(self) -> int:
        return len(self.get_items)


class Shop(Storage):
    """
    Класс магазина товаров
    """

    def __init__(self):
        super().__init__()
        self._capacity = 20

    def __repr__(self):
        if len(self.get_items) == 0:
            return f'В магазине пусто! Вместимость: {self._capacity}.'
        return 'В магазине хранятся:\n' + '\n'.join(f'> {amount} {item}' for item, amount in self.get_items.items())

    def add(self, title: str, qty: int) -> bool:
        if self.get_unique_items_count() == 5 and title not in self.get_items:
            print('Невозможно доставить товар в магазин. В магазине уже 5 видов различных товаров.\n')
        elif self.get_free_space() >= qty:
            if title not in self.get_items:
                self._items[title] = 0
            self._items[title] += qty
            return True
        else:
            print('В магазине недостаточно места!\n')
        return False

    def remove(self, title: str, qty: int) -> bool:
        if title in self.get_items:
            if qty <= self.get_items[title]:
                self.get_items[title] -= qty
                if self.get_items[title] == 0:
                    self.delete_item(title)
                return True
            else:
                print(f'Не достаточно товара "{title}" в магазине! Попробуйте заказать меньше!\n')
        else:
            print(f'Данного товара нет в магазине!\n')
        return False

    def delete_item(self, title):
        del self._items[title]

    @property
    def get_items(self) -> dict[str: int]:
        return self._items

    def get_free_space(self) -> int:
        return self._capacity - sum(self.get_items.values())

    def get_unique_items_count(self) -> int:
        return len(self.get_items)


class BadRequest(Exception):
    pass


class Request:
    """
    Класс запроса от пользователя
    """

    def __init__(self, request: str):
        match request.split():
            case _, amount, product, _, from_storage, _, _:  # "Доставить 3 бананы из склад в магазин"
                pass
            case _, _, amount, product, _, from_storage:  # "Курьер забирает 2 кофе из склад (магазин)"
                pass
            case _:
                raise BadRequest('Ошибка: Неверный формат запроса.')
        if amount.isdigit():
            self._amount = int(amount)
        else:
            raise BadRequest('Ошибка: Неверный формат запроса.')
        self._product = product
        if 'магазин' in from_storage:
            self._from, self._to = 'магазин', 'склад'
        else:
            self._from, self._to = 'склад', 'магазин'

    @property
    def get_data(self):
        return self._from, self._to, self._product, self._amount

    def __repr__(self):
        return f'<Request: from "{self._from}" to "{self._to}", product "{self._product}", amount "{self._amount}">'
