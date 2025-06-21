import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestUserJourney(unittest.TestCase):
    def setUp(self):
        # Укажите путь к драйверу ChromeDriver или используйте PATH по умолчанию.
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_search_and_purchase_book(self):
        driver = self.driver

        # Заходим на главную страницу магазина
        driver.get("http://localhost:8000")  # замените на актуальный URL

        # Вводим название книги в поле поиска
        search_box = driver.find_element(By.ID, "search-input")
        search_box.send_keys("Мастер и Маргарита")
        search_box.send_keys(Keys.RETURN)

        # Проверяем, что в зоне внимания появляется нужная книга (например, по названию)
        results = driver.find_elements(By.CLASS_NAME, "book-title")
        
        found = any("Мастер и Маргарита" in el.text for el in results)
        
        self.assertTrue(found, "Книга не найдена в результатах поиска.")

        # Добавляем книгу в корзину (предположим есть кнопка с классом "add-to-cart")
        for el in results:
            if "Мастер и Маргарита" in el.text:
                add_button = el.find_element(By.XPATH, "../button[@class='add-to-cart']")
                add_button.click()
                break

        # Переходим к оформлению заказа (например, по ссылке или кнопке)
        driver.find_element(By.ID, "cart-link").click()
        
        # Заполняем форму заказа (имя и адрес)
        driver.find_element(By.ID, "name").send_keys("Иван Иванов")
        driver.find_element(By.ID, "address").send_keys("ул. Ленина, д.1")
        
        # Подтверждаем покупку
        driver.find_element(By.ID, "submit-order").click()

        # Проверяем появление страницы «Спасибо за заказ»
        header_text = driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Спасибо за заказ", header_text)

if __name__ == "__main__":
    unittest.main()
