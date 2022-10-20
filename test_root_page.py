import allure
import pytest

from locators import RootPageLocators
from pages.root import RootPage


class TestRootPage:

    @allure.title('Проверка ответа на вопрос')
    @pytest.mark.parametrize(
        'question_locator,answer_locator,answer,question_number',
        (
                (question_locator, answer_locator, answer, question_number) for
                question_locator, answer_locator, answer, question_number in
                zip(RootPageLocators.questions, RootPageLocators.answers, RootPage.answers,
                    range(1, len(RootPageLocators.questions) + 1))
        )
    )
    def test_question(self, driver, question_locator, answer_locator, answer, question_number):
        page = RootPage(driver)
        page.open()
        page.scroll_to_element(question_locator)
        page.click_on_question(question_locator)
        assert driver.find_element(*answer_locator).text == answer, \
            f'Ответ на вопрос {question_number} не совпадает с ожидаемым'

    @allure.title('Пользователь может перейти на страницу заказа через верхнюю кнопку заказа')
    def test_go_to_order_page_via_upper_order_button(self, driver):
        driver.implicitly_wait(3)
        page = RootPage(driver)
        page.open()
        driver.find_element(*RootPageLocators.button_order_top).click()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order', 'Переход на страницу заказа не совершен'

    @allure.title('Пользователь может перейти на страницу заказа через нижнюю кнопку заказа')
    def test_go_to_order_page_via_bottom_order_button(self, driver):
        driver.implicitly_wait(3)
        page = RootPage(driver)
        page.open()
        button = driver.find_element(*RootPageLocators.button_order_bottom)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/order', 'Переход на страницу заказа не совершен'

    @allure.title('Пользователь может перейти на страницу Яндекс.Дзена')
    def test_customer_can_go_to_yandex_page(self, driver):
        driver.implicitly_wait(3)
        page = RootPage(driver)
        page.open()

        page.click_on_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])

        current_link = page.get_url_with_waiting()

        # необходимо одновременно получить ссылку в AssertionError (а не Bool-value) и проверить несколько значений
        assert 'yandex.ru' in current_link or current_link == 'https://dzen.ru/?yredirect=true', 'Не был осуществлен переход на Яндекс или Дзен'
