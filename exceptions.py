class NotEnoughSpace(BaseException):
    message = 'Невозможно доставить товар, недостаточно места!\n'


class NotEnoughGoods(BaseException):
    message = 'Не достаточно товара! Попробуйте заказать меньше!\n'


class NoGoodsInStorage(BaseException):
    message = 'Данного товара нет на складе!\n'


class MaxUniqueItemsInStorage(BaseException):
    message = 'Невозможно доставить товар!\n'


class BadRequest(BaseException):
    message = 'Неверный формат запроса. Попробуйте заново!\n'
