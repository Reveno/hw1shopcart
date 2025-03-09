# shopping_cart.py

class ShoppingCart:
    def __init__(self):
        # Кошик зберігає товари як словник {назва товару: ціна}
        self.items = {}

    def add_item(self, item, price):
        """
        Додає товар із вказаною ціною до кошика.
        :param item: Назва товару
        :param price: Ціна товару
        """
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Ціна має бути додатнім числом")
        self.items[item] = price

    def remove_item(self, item):
        """
        Видаляє товар із кошика.
        :param item: Назва товару для видалення
        """
        if item not in self.items:
            raise ValueError("Товар не знайдено в кошику")
        del self.items[item]

    def get_total(self):
        """
        Повертає загальну вартість товарів у кошику.
        :return: Загальна вартість
        """
        return sum(self.items.values())

    def apply_discount(self, discount):
        """
        Застосовує знижку до всіх товарів у кошику.
        :param discount: Відсоток знижки (0-100)
        """
        if not isinstance(discount, (int, float)) or discount < 0 or discount > 100:
            raise ValueError("Знижка має бути числом від 0 до 100")
        for item in self.items:
            self.items[item] *= (1 - discount / 100)
