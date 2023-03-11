from class_base_storage import BaseStorage
from exceptions import BadRequest


class Request:
    """
    Класс оформления запроса от пользователя
    """

    def __init__(self, request: str, storages: dict[str: BaseStorage]):
        match request.split():
            case _, amount, product, _, from_, _, to_:  # "Доставить 3 бананы из склад в магазин"
                pass
            case _:
                raise BadRequest()

        if amount.isdigit() and from_ in storages and to_ in storages:
            self.amount = int(amount)
            self.from_storage = from_
            self.to_storage = to_
            self.product = product
        else:
            raise BadRequest()

    def __repr__(self):
        return f'<Request: from "{self.from_storage}" to "{self.to_storage}", ' \
               f'product "{self.product}", amount "{self.amount}">'
