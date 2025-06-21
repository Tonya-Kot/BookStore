# BookStore
Компания «BookStore», которая разрабатывает веб-приложение для онлайн-продажи книг.
# Автоматизация тестирования для BookStore

## Установка зависимостей

```bash
pip install selenium pytest pytest-headless

pytest tests/test_calculate_total_price.py

pytest tests/test_integration_cart_payment.py

pytest tests/test_ui_search_order.py --headless
