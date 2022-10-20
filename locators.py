from selenium.webdriver.common.by import By


class RootPageLocators:
    questions = (
        (By.XPATH, "//div[@id='accordion__heading-0']"),
        (By.XPATH, "//div[@id='accordion__heading-1']"),
        (By.XPATH, "//div[@id='accordion__heading-2']"),
        (By.XPATH, "//div[@id='accordion__heading-3']"),
        (By.XPATH, "//div[@id='accordion__heading-4']"),
        (By.XPATH, "//div[@id='accordion__heading-5']"),
        (By.XPATH, "//div[@id='accordion__heading-6']"),
        (By.XPATH, "//div[@id='accordion__heading-7']"),
    )

    answers = (
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


class OrderPageLocators:
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


class BasePageLocators:
    img_logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    img_logo_yandex = (By.XPATH, '//img[@alt="Yandex"]')
