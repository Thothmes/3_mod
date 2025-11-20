import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_cart_button_presence(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Задержка для визуальной проверки языка
    time.sleep(20)

    # Проверяем наличие кнопки добавления в корзину. find_elements используем, поскольку в отличие от find_element он возвращает список
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    print(add_to_cart_button)

    # Утверждение, что кнопка найдена
    assert len(add_to_cart_button) > 0, "Add to cart button is not found on the page"

    # Дополнительная проверка, что кнопка видима
    assert add_to_cart_button[0].is_displayed(), "Add to cart button is not visible"
    assert add_to_cart_button[0].is_enabled(), "Add to cart button is not enabled"