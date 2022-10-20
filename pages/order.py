from random import randint, choice

from selenium.webdriver import Keys

from locators import OrderPageLocators
from .base import BasePage


class AboutCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_name_field(self, name):
        self.driver.find_element(*OrderPageLocators.input_name).send_keys(name)

    def fill_surname_field(self, surname):
        self.driver.find_element(*OrderPageLocators.input_surname).send_keys(surname)

    def fill_phone_field(self, phone):
        self.driver.find_element(*OrderPageLocators.input_phone).send_keys(phone)

    def fill_address_field(self, address):
        self.driver.find_element(*OrderPageLocators.input_address).send_keys(address)

    def fill_metro_dropdown(self):
        self.driver.find_element(*OrderPageLocators.dropdown_metro_station).click()
        self.driver.find_element(*OrderPageLocators.dropdown_metro_station).send_keys(Keys.DOWN)
        self.driver.find_element(*OrderPageLocators.dropdown_metro_station).send_keys(Keys.ENTER)

    def fill_time_dropdown(self):
        self.driver.find_element(*OrderPageLocators.dropdown_calendar).click()
        self.driver.find_element(*OrderPageLocators.dropdown_calendar).send_keys(Keys.ENTER)

    def click_go_next_button(self):
        self.driver.find_element(*OrderPageLocators.button_go_next).click()


class AboutRentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_rental_period(self):
        self.driver.find_element(*OrderPageLocators.dropdown_rental_period).click()
        time_range_options = self.driver.find_elements(*OrderPageLocators.dropdown_rental_option)
        time_range_option = time_range_options[randint(0, 6)]
        time_range_option.click()

    def fill_address(self, address):
        self.driver.find_element(*OrderPageLocators.input_address).send_keys(address)

    def fill_scooter_color(self):
        self.driver.find_element(
            *choice(
                (
                    OrderPageLocators.checkbox_kick_scooter_color_black,
                    OrderPageLocators.checkbox_kick_scooter_color_grey
                )
            )
        ).click()

    def fill_comment_field(self, comment):
        self.driver.find_element(*OrderPageLocators.input_comment).send_keys(comment)

    def click_purchase_button(self):
        self.driver.find_element(*OrderPageLocators.button_purchase).click()


class OrderPage(AboutCustomerPage, AboutRentPage, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

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
        self.driver.find_element(*OrderPageLocators.button_confirm).click()

