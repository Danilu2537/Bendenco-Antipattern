from class_base_storage import BaseStorage


class Storage(BaseStorage):
    """
    Cклад товаров
    """

    def __init__(self):
        super().__init__()
        self._capacity = 100

    def __repr__(self):
        if len(self.get_items) == 0:
            return f'На складе пусто! Вместимость: {self._capacity}.'
        return 'На складе хранятся:\n' + '\n'.join(f'> {amount} {item}' for item, amount in self.get_items.items())
