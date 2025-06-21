def calculate_total_price(items):
    """
    Подсчитывает итоговую стоимость товаров.
    :param items: список словарей с ключами 'name' и 'price'
    :return: сумма цен товаров
    """
    total = sum(item['price'] for item in items)
    return total
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def clear(self):
        self.items = []

def process_payment(cart, amount):
    """
    Имитация обработки платежа.
    Если сумма положительна, платеж успешен.
    """
    if amount > 0:
        cart.clear()
        return True
    return False
