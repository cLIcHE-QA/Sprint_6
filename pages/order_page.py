import random

import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Нажать на кнопку «Заказать»")
    def click_to_order_button_header(self):
        self.click_to_element(BasePageLocators.ORDER_BUTTON)

    @allure.step("Проскроллить до кнопки «Заказать» внизу страницы")
    def scroll_to_order_button_down(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.find_definite_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Нажать на кнопку «Заказать» внизу страницы")
    def click_to_order_button_down(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Нажать на кнопку «Да все привыкли»")
    def click_to_cookie_button(self):
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)

    @allure.step("Заполнить поле «Имя»")
    def set_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.NAME_FIELD, text)

    @allure.step("Заполнить поле «Фамилия»")
    def set_lastname_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FIELD, text)

    @allure.step("Заполнить поле «Адрес»")
    def set_address_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FIELD, text)

    @allure.step("Нажать на поле «Метро»")
    def click_to_metro(self):
        self.click_to_element(OrderPageLocators.METRO_FIELD)

    @allure.step("Выбрать станцию метро")
    def choose_metro_station(self):
        method, locator = OrderPageLocators.CHOOSE_METRO
        intervals = [(1, 79), (92, 237)]
        chosen_interval = random.choice(intervals)
        number = random.randint(chosen_interval[0], chosen_interval[1])
        locator = locator.format(num=number)
        self.click_to_element((method, locator))

    @allure.step("Заполнить поле «Телефон»")
    def set_phone_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.PHONE_FIELD, text)

    @allure.step("Нажать на кнопку «Далее»")
    def click_to_onward_button(self):
        self.click_to_element(OrderPageLocators.ONWARD_BUTTON)

    @allure.step("Заполнить поле «Когда привезти самокат»")
    def set_date_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.WHEN_FIELD, text)

    @allure.step("Нажать на выбранную дату в календаре")
    def click_to_choose_date(self):
        self.click_to_element(OrderPageLocators.CHOOSE_DATE)

    @allure.step("Нажать на поле «Срок аренды»")
    def click_to_rent_date(self):
        self.click_to_element(OrderPageLocators.LIMIT_FIELD)

    @allure.step("Выбрать вариант из списка «Срок аренды»")
    def choose_date(self):
        options = self.find_option_elements(OrderPageLocators.CHOOSE_LIMIT)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Выбрать самокат")
    def choose_scooter(self):
        options = self.find_option_elements(OrderPageLocators.CHOOSE_SCOOTER)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Добавить комментарий для курьера")
    def set_comment_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.COMMENT_FIELD, text)

    @allure.step("Нажать на кнопку «Заказать под формой»")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_UNDER_FORM)

    @allure.step("Подтвердить заказ")
    def click_to_confirm_button(self):
        self.click_to_element(OrderPageLocators.AGREE_BUTTON)

    @allure.step("Проверить статус заказа")
    def check_success_order(self):
        return self.find_definite_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step("Нажать на кнопку «Посмотреть статус»")
    def click_to_status_button(self):
        self.click_to_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step("Проверить, что перешли на страницу заказа")
    def check_order_page(self):
        return self.find_definite_element(OrderPageLocators.CANCEL_BUTTON)

    @allure.step("Создание заказа")
    def create_order(self, name, lastname, address, phone, date, comment):
        self.set_name_to_field(name)
        self.set_lastname_to_field(lastname)
        self.set_address_to_field(address)
        self.click_to_metro()
        self.choose_metro_station()
        self.set_phone_to_field(phone)
        self.click_to_onward_button()
        self.set_date_to_field(date)
        self.click_to_choose_date()
        self.click_to_rent_date()
        self.choose_date()
        self.choose_scooter()
        self.set_comment_to_field(comment)
        self.click_to_order_button()
        self.click_to_confirm_button()
        self.check_success_order()
        self.click_to_status_button()
