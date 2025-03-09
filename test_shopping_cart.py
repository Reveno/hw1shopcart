# test_shopping_cart.py

import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # Створюємо новий об'єкт кошика перед кожним тестом
        self.cart = ShoppingCart()

    def test_add_item(self):
        """
        Тест для методу add_item.
        Перевіряє правильність додавання товару до кошика.
        """
        # Перевіряємо, що товар додається з правильною ціною
        self.cart.add_item("apple", 1.0)
        self.assertEqual(self.cart.items["apple"], 1.0)

        # Перевіряємо, що виникає помилка при спробі додати товар з негативною ціною
        with self.assertRaises(ValueError):
            self.cart.add_item("banana", -1)

        # Перевіряємо, що виникає помилка при спробі додати товар з ціною, яка не є числом
        with self.assertRaises(ValueError):
            self.cart.add_item("banana", "two")

    def test_remove_item(self):
        """
        Тест для методу remove_item.
        Перевіряє правильність видалення товару з кошика.
        """
        # Додаємо товар і видаляємо його, перевіряючи, що він більше немає в кошику
        self.cart.add_item("apple", 1.0)
        self.cart.remove_item("apple")
        self.assertNotIn("apple", self.cart.items)

        # Перевіряємо, що виникає помилка при спробі видалити неіснуючий товар
        with self.assertRaises(ValueError):
            self.cart.remove_item("banana")

    def test_get_total(self):
        """
        Тест для методу get_total.
        Перевіряє правильність обчислення загальної вартості товарів у кошику.
        """
        # Додаємо товари і перевіряємо, що загальна вартість обчислюється правильно
        self.cart.add_item("apple", 1.0)
        self.cart.add_item("banana", 2.0)
        self.assertEqual(self.cart.get_total(), 3.0)

    def test_apply_discount(self):
        """
        Тест для методу apply_discount.
        Перевіряє правильність застосування знижки до всіх товарів у кошику.
        """
        # Додаємо товар, застосовуємо знижку і перевіряємо, що ціна змінилася правильно
        self.cart.add_item("apple", 100.0)
        self.cart.apply_discount(10)
        self.assertEqual(self.cart.items["apple"], 90.0)

        # Перевірка на помилку при спробі негативної знижки ( мінус перед цифрою)
        with self.assertRaises(ValueError):
            self.cart.apply_discount(-10)

        # Перевірка на помилку при спробі знижки більше 100%
        with self.assertRaises(ValueError):
            self.cart.apply_discount(110)

        #  Перевірка на помилку при знижці, що написана не цифрами
        with self.assertRaises(ValueError):
            self.cart.apply_discount("ten")

if __name__ == '__main__':
    # Запуск тестів при виконанні цього файлу
    unittest.main()
