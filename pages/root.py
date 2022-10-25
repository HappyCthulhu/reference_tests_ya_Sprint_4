from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class RootPage(BasePage):
    def __init__(self, driver: Firefox):
        super().__init__(driver)

    answers = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
    ]

    questions_locators = (
        (By.XPATH, "//div[@id='accordion__heading-0']"),
        (By.XPATH, "//div[@id='accordion__heading-1']"),
        (By.XPATH, "//div[@id='accordion__heading-2']"),
        (By.XPATH, "//div[@id='accordion__heading-3']"),
        (By.XPATH, "//div[@id='accordion__heading-4']"),
        (By.XPATH, "//div[@id='accordion__heading-5']"),
        (By.XPATH, "//div[@id='accordion__heading-6']"),
        (By.XPATH, "//div[@id='accordion__heading-7']"),
    )

    answers_locators = (
        (By.XPATH, "//div[@id='accordion__panel-0']/p"),
        (By.XPATH, "//div[@id='accordion__panel-1']/p"),
        (By.XPATH, "//div[@id='accordion__panel-2']/p"),
        (By.XPATH, "//div[@id='accordion__panel-3']/p"),
        (By.XPATH, "//div[@id='accordion__panel-4']/p"),
        (By.XPATH, "//div[@id='accordion__panel-5']/p"),
        (By.XPATH, "//div[@id='accordion__panel-6']/p"),
        (By.XPATH, "//div[@id='accordion__panel-7']/p"),
    )

    button_order_top = (By.XPATH, '(//button[contains(@class, "Button_Button")])[1]')
    button_order_bottom = (By.XPATH, '//button[contains(@class, "Button_UltraBig")]')

    def open(self):
        return self.driver.get('https://qa-scooter.praktikum-services.ru/')

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_question(self, question_xpath):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(question_xpath)).click()
