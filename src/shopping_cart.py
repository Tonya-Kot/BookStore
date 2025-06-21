def calculate_total_price(items):
    """
    Подсчитывает итоговую стоимость товаров.
    :param items: список словарей с ключами 'name' и 'price'
    :return: сумма цен товаров
    """
    total = sum(item['price'] for item in items)
    return total
