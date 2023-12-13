import time

from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # Временная задержка для наглядности
    time.sleep(30)
    # Проверка наличии кнопки
    buttonAddCart = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert buttonAddCart, "Add to cart button is not present"

