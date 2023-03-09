from classes import Store, Shop, Request, BadRequest


def main():
    print('Welcome to the Logistics App!')
    print('Отправьте запрос в формате:'
          ' "Доставить 5 бананы со склада в магазин" или "Курьер берёт 3 кофе из магазина"\n')

    while True:
        user_input = input()
        request = None
        try:
            request = Request(user_input)
        except BadRequest as e:
            print(f'{e}\nПопробуйте отправить запрос заново в верном формате!\n')
        if request:
            from_, to_, product, amount = request.get_data
            if 'склад' in from_:
                delivery_path = (storage, shop)
            else:
                delivery_path = (shop, storage)
            if delivery_path[0].remove(product.capitalize(), amount):
                if not delivery_path[1].add(product.capitalize(), amount):
                    delivery_path[0].add(product.capitalize(), amount)
                else:
                    print(f'Нужное количество есть {"на" if from_ == "склад" else "в"} {from_}е')
                    print(f'Курьер забрал {amount} {product} {"со" if from_ == "склад" else "из"} {from_}а')
                    print(f'Курьер везёт {amount} {product} из {from_}а {"на" if to_ == "склад" else "в"} {to_}')
                    print(f'Курьер доставил {amount} {product} {"на" if to_ == "склад" else "в"} {to_}\n')
                    print('*' * 20)
                    print(storage)
                    print('*' * 20)
                    print(shop)
                    print('*' * 20)


if __name__ == '__main__':
    storage = Store()

    storage.add('Масло', 10)
    storage.add('Макароны', 20)
    storage.add('Апельсины', 10)
    storage.add('Бананы', 20)
    storage.add('Кофе', 10)
    storage.add('Чай', 10)
    storage.add('Шоколад', 5)
    storage.add('Хлеб', 6)

    shop = Shop()

    shop.add('Бананы', 5)
    shop.add('Кофе', 4)
    shop.add('Чай', 3)

    main()
