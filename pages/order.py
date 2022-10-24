from random import randint, choice

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from .base import BasePage


class AboutCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, name):
        self.driver.find_element(*OrderPage.input_name).send_keys(name)

    def fill_surname_field(self, surname):
        self.driver.find_element(*OrderPage.input_surname).send_keys(surname)

    def fill_phone_field(self, phone):
        self.driver.find_element(*OrderPage.input_phone).send_keys(phone)

    def fill_address_field(self, address):
        self.driver.find_element(*OrderPage.input_address).send_keys(address)

    def fill_metro_dropdown(self):
        self.driver.find_element(*OrderPage.dropdown_metro_station).click()
        self.driver.find_element(*OrderPage.dropdown_metro_station).send_keys(Keys.DOWN)
        self.driver.find_element(*OrderPage.dropdown_metro_station).send_keys(Keys.ENTER)

    def fill_time_dropdown(self):
        self.driver.find_element(*OrderPage.dropdown_calendar).click()
        self.driver.find_element(*OrderPage.dropdown_calendar).send_keys(Keys.ENTER)

    def click_go_next_button(self):
        self.driver.find_element(*OrderPage.button_go_next).click()


class AboutRentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_rental_period(self):
        self.driver.find_element(*OrderPage.dropdown_rental_period).click()
        time_range_options = self.driver.find_elements(*OrderPage.dropdown_rental_option)
        time_range_option = time_range_options[randint(0, 6)]
        time_range_option.click()

    def fill_address(self, address):
        self.driver.find_element(*OrderPage.input_address).send_keys(address)

    def fill_scooter_color(self):
        self.driver.find_element(
            *choice(
                (
                    OrderPage.checkbox_kick_scooter_color_black,
                    OrderPage.checkbox_kick_scooter_color_grey
                )
            )
        ).click()

    def fill_comment_field(self, comment):
        self.driver.find_element(*OrderPage.input_comment).send_keys(comment)

    def click_purchase_button(self):
        self.driver.find_element(*OrderPage.button_purchase).click()


class OrderPage(AboutCustomerPage, AboutRentPage, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    input_name = (By.XPATH, '//input[@placeholder="* Имя"]')
    input_surname = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    input_address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    dropdown_metro_station = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    input_phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    # TODO: подобрать локатор без динамического префикса
    button_go_next = (By.XPATH, '//button[contains(text(), "Далее")]')
    dropdown_calendar = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    dropdown_rental_period = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    dropdown_rental_option = (By.XPATH, '//div[@class="Dropdown-option"]')
    checkbox_kick_scooter_color_black = (By.XPATH, '//input[@id="black"]')
    checkbox_kick_scooter_color_grey = (By.XPATH, '//input[@id="grey"]')
    input_comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    button_go_back = (By.XPATH,
                      '//button[contains(@class, "Button_Inverted")]')  # contains() нужен, ибо классы динамические. Присутствуют постфиксы
    button_purchase = (By.XPATH, '//button[contains(@class, "Button_Middle")][2]')
    button_confirm = (By.XPATH, '//button[contains(text(),"Да")]')
    button_decline = (By.XPATH, '//button[contains(text(),"Нет")]')
    text_purchase_details = (By.XPATH, '//div[contains(@class, "Order_Text")]')

    def open(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

    def process_about_customer_page(self, name, surname, phone, address):
        self.fill_name_field(name)
        self.fill_surname_field(surname)
        self.fill_phone_field(phone)
        self.fill_address_field(address)
        self.fill_metro_dropdown()
        self.click_go_next_button()

    def process_about_rent_page(self, comment):
        self.fill_time_dropdown()
        self.fill_rental_period()
        self.fill_scooter_color()
        self.fill_comment_field(comment)
        self.click_purchase_button()

    def confirm_purchase(self):
        self.driver.find_element(*OrderPage.button_confirm).click()
