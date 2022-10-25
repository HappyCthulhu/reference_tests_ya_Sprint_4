from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    img_logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    img_logo_yandex = (By.XPATH, '//img[@alt="Yandex"]')

    def click_on_scooter_logo(self):
        self.driver.find_element(*BasePage.img_logo_scooter).click()

    def click_on_yandex_logo(self):
        self.driver.find_element(*BasePage.img_logo_yandex).click()

    # функция нужна, чтобы мы получали AssertError в тестах, а не TimeoutException
    def get_url_with_waiting(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                # any_of необходима из-за того, что yandex периодически выдает капчу + ожидание необходимо
                EC.any_of(EC.url_to_be('https://dzen.ru/?yredirect=true'), EC.url_contains('yandex.ru')))
        except TimeoutException:
            pass

        return self.driver.current_url

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
