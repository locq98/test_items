import time
from selenium.webdriver.common.by import By

class TestButton():
    def test_purchase_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        button = len(browser.find_elements(By.CSS_SELECTOR, "button.btn:nth-child(3)"))
        assert button > 0, 'Кнопка не найдена'
        time.sleep(30)
