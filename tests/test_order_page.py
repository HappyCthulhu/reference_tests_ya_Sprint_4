import allure
from selenium.webdriver import Firefox

from pages.order import OrderPage
from pages.root import RootPage


class TestOrderPage:
    @allure.title('Проверка возможности сделать заказ')
    def test_customer_can_make_order_via_upper_button(self, driver: Firefox, name, surname, phone, address, comment):
        page = RootPage(driver)
        page.open()
        driver.find_element(*RootPage.button_order_top).click()

        page = OrderPage(driver)

        page.process_about_customer_page(name, surname, phone, address)
        page.process_about_rent_page(comment)
        page.confirm_purchase()

        elem_text = driver.find_element(*OrderPage.text_purchase_details).text
        purchase_numbers = elem_text.split('Номер заказа:')[1].split('.')[0].strip()

        assert purchase_numbers.isnumeric()

    def test_customer_can_make_order_via_bottom_button(self, driver: Firefox, name, surname, phone, address, comment):
        page = RootPage(driver)
        page.open()
        page.scroll_to_element(RootPage.button_order_bottom)
        driver.find_element(*RootPage.button_order_bottom).click()

        page = OrderPage(driver)

        page.process_about_customer_page(name, surname, phone, address)
        page.process_about_rent_page(comment)
        page.confirm_purchase()

        elem_text = driver.find_element(*OrderPage.text_purchase_details).text
        purchase_numbers = elem_text.split('Номер заказа:')[1].split('.')[0].strip()

        assert purchase_numbers.isnumeric()

    @allure.title('Проверка возможности перехода на корневую страницу')
    def test_customer_can_go_to_root_page(self, driver):
        page = OrderPage(driver)
        page.open()

        page.click_on_scooter_logo()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка возможности перехода на страницу Яндекс.Дзен')
    def test_customer_can_go_to_yandex_page(self, driver):
        page = OrderPage(driver)
        page.open()

        page.click_on_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])

        current_link = page.get_url_with_waiting()

        # необходимо одновременно получить ссылку в AssertionError (а не Bool-value) и проверить несколько значений
        assert 'yandex.ru' in current_link or current_link == 'https://dzen.ru/?yredirect=true', 'Не был осуществлен переход на Яндекс или Дзен'
