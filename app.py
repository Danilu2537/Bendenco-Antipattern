from class_request import Request
from class_shop import Shop
from class_storage import Storage
from exceptions import BadRequest, NoGoodsInStorage, NotEnoughGoods, NotEnoughSpace, MaxUniqueItemsInStorage


def main():
    print('Welcome to the Logistics App!')
    print('Отправьте запрос в формате: "Доставить 5 бананы из склад в магазин"\n')

    while True:
        user_input = input()

        try:
            request = Request(user_input, storages)
        except BadRequest as error:
            print(error.message)
            continue

        delivery_from = storages[request.from_storage]
        delivery_to = storages[request.to_storage]

        # Try to get goods from a storage 1
        try:
            delivery_from.remove(request.product.capitalize(), request.amount)
        except (NoGoodsInStorage, NotEnoughGoods) as error:
            print(error.message)
            continue

        # Try to deliver goods from a storage 1 to a storage 2.
        # If not possible returns goods back to a storage 1
        try:
            delivery_to.add(request.product.capitalize(), request.amount)
        except (NotEnoughSpace, MaxUniqueItemsInStorage) as error:
            delivery_from.add(request.product.capitalize(), request.amount)
            print(error.message)
            continue

        print(f'Нужное количество есть в {request.from_storage}')
        print(f'Курьер забрал {request.amount} {request.product} из {request.from_storage}')
        print(f'Курьер везёт {request.amount} {request.product} из {request.from_storage} в {request.to_storage}')
        print(f'Курьер доставил {request.amount} {request.product} в {request.to_storage}\n')
        print('*' * 20)
        print(storage)
        print('*' * 20)
        print(shop)
        print('*' * 20)


if __name__ == '__main__':
    storage = Storage()
    shop = Shop()

    storages = {
        'магазин': shop,
        'склад': storage,
    }

    storage.add('Масло', 10)
    storage.add('Макароны', 20)
    storage.add('Апельсины', 10)
    storage.add('Бананы', 20)
    storage.add('Кофе', 10)
    storage.add('Чай', 10)
    storage.add('Шоколад', 5)
    storage.add('Хлеб', 6)

    shop.add('Бананы', 5)
    shop.add('Кофе', 4)
    shop.add('Чай', 3)

    main()
