import time
from selenium.webdriver.common.by import By

class TestLanguageButton():
    def test_buy_button_es(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        text_value = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button').text
        assert 'Añadir al carrito' in text_value
        time.sleep(30)
